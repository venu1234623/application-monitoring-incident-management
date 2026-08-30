# Application Monitoring & Incident Management System

A Python-based application monitoring and incident management system designed to monitor application health, detect failures, and automatically create incidents when an application becomes unavailable.

## Features

- Application health monitoring
- HTTP health-check endpoint validation
- Response time measurement
- Detection of application failures
- Automatic incident creation
- Incident status tracking
- SQLite database storage
- Web-based monitoring dashboard
- REST API endpoint for monitoring
- Automated tests using Python

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- REST API
- Requests
- Pytest
- Git & GitHub

## Project Structure

```text
application-monitoring-incident-management/
│
├── app/
│   ├── database/
│   │   ├── database.py
│   │   └── test_database.py
│   │
│   ├── incidents/
│   │   ├── incident_manager.py
│   │   └── test_incident.py
│   │
│   ├── monitoring/
│   │   ├── health_checker.py
│   │   ├── health_server.py
│   │   └── test_monitor.py
│   │
│   ├── templates/
│   │   └── dashboard.html
│   │
│   └── app.py
│
├── .gitignore
├── requirements.txt
└── README.md