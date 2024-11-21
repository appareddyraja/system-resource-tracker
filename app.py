from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import psutil
import threading
import time

app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create an SQLAlchemy instance
db = SQLAlchemy(app)

# Define the Profile model
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    cpu = db.Column(db.Float, nullable=False)
    ram = db.Column(db.Float, nullable=False)
    disk = db.Column(db.Float, nullable=False)

# Background task to continuously collect and store metrics
def collect_metrics():
    with app.app_context():
        while True:
            try:
                # Collect system metrics
                cpu = psutil.cpu_percent(1)
                ram = psutil.virtual_memory().percent
                disk = psutil.disk_usage('/').percent

                # Save metrics to the database
                new_profile = Profile(cpu=cpu, ram=ram, disk=disk)
                db.session.add(new_profile)
                db.session.commit()
            except Exception as e:
                print(f"Error storing metrics: {e}")

            # Sleep for a defined interval (e.g., 60 seconds)
            time.sleep(60)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/metrics')
def get_metrics():
    # Retrieve metrics data from the database
    profiles = Profile.query.order_by(Profile.time).all()
    times = [profile.time.strftime('%Y-%m-%d %H:%M:%S') for profile in profiles]
    cpu = [profile.cpu for profile in profiles]
    ram = [profile.ram for profile in profiles]
    disk = [profile.disk for profile in profiles]

    # Return data in JSON format
    return jsonify({'times': times, 'cpu': cpu, 'ram': ram, 'disk': disk})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist

    # Start the background thread
    thread = threading.Thread(target=collect_metrics, daemon=True)
    thread.start()

    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)