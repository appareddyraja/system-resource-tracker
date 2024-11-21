# System Metrics Monitoring Flask App

## Overview
This is a Flask-based web application that continuously monitors and visualizes system metrics, including CPU, RAM, and disk usage. The application collects metrics every minute and stores them in an SQLite database, with a web interface to display the data.

## Features
- Real-time system metrics tracking
- Background metric collection
- Persistent storage of historical metrics
- Web-based visualization
- Supports running on any host and port

## Prerequisites
- Python 3.8+
- Flask
- SQLAlchemy
- psutil

## Installation

### 1. Clone the Repository
```
git clone https://github.com/appareddyraja/system-resource-tracker.git
cd system-resource-tracker
```

### 2. Create a Virtual Environment (Optional but Recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```pip install flask flask-sqlalchemy psutil```

## Project Structure
```
.
├── README.md
├── app.py           # Main Flask application
├── instance/
│   └── site.db      # SQLite database (auto-generated)
└── templates/
    └── index.html   # Web interface template
```

## Configuration
- Database: SQLite (automatically created in `instance/site.db`)
- Metrics Collection Interval: 60 seconds
- Host: 0.0.0.0
- Port: 5000

## Running the Application
```
python app.py
```

## Metrics Tracked
- CPU Usage (%)
- RAM Usage (%)
- Disk Usage (%)

## Endpoints
- `/`: Web interface displaying system metrics
- `/metrics`: JSON endpoint for metrics data

## How It Works
1. Background thread collects system metrics every minute
2. Metrics are stored in an SQLite database
3. Web interface retrieves and displays historical metrics

## Performance Considerations
- Metrics are sampled at 1-second intervals
- Database stores metrics every 60 seconds
- Uses a daemon thread for background processing

## Customization
Modify `app.py` to:
- Change metrics collection interval
- Adjust database storage duration
- Add more system metrics

## Potential Improvements
- Add authentication
- Implement data retention policies
- Create more advanced visualizations
- Support multiple database backends

## Dependencies
- Flask
- Flask-SQLAlchemy
- psutil

## License
MIT

## Author
```Appareddy```
