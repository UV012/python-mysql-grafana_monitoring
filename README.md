# 📊 System Metrics Monitoring with Python, MySQL & Grafana

## 📌 Project Overview

This project implements a lightweight system monitoring pipeline that:
- Collects **CPU and Memory usage** from a Linux system
- Stores metrics in a **MySQL database**
- Logs execution details to a file
- Visualizes real-time metrics using **Grafana dashboards**

It simulates a real-world infrastructure monitoring setup commonly used in DevOps and production environments.

## 🏗️ Architecture

```
+----------------+
|  Linux Server  |
|----------------|
| metrics_collector.py
| (psutil)       |
+--------+-------+
         |
         v
+----------------+
|     MySQL      |
| mysql-grafana_monitoring DB
| system_metrics |
+--------+-------+
         |
         v
+----------------+
|    Grafana     |
|  Dashboard     |
+----------------+
```

## ⚙️ Tech Stack
- **Python 3**
- `psutil` – system metrics collection
- `mysql-connector-python` – MySQL integration
- **MySQL** – metrics storage
- **Grafana** – visualization
- Linux (Tested on Ubuntu VM)

## 📁 Project Structure

```
python-mysql-grafana_monitoring/
│
├── metrics_collector.py
├── logs/
│   └── metrics.log
└── README.md
```

## 🧠 How It Works
1. Script collects:
   - CPU usage (%)
   - Memory usage (%)
2. Connects to MySQL database.
3. Inserts metrics into `system_metrics` table.
4. Logs success or error into:
   `/opt/python-mysql-grafana_monitoring/logs/metrics.log`

## 🛠️ Installation & Setup

### 1️⃣ Create virtual environment (recommended)
```bash
cd /path/to/folder
python3 -m venv venv
source venv/bin/activate
pip install psutil mysql-connector-python
```

### 2️⃣ Install System Dependencies
```
sudo apt update
sudo apt install mysql-server python3-pip
pip3 install psutil mysql-connector-python
```

### 3️⃣ Setup MySQL Database
Login to MySQL:

` sudo mysql `

Create database and user:

```
CREATE DATABASE mysql-grafana_monitoring;

CREATE USER 'user'@'localhost' IDENTIFIED BY 'YourPassword';

GRANT ALL PRIVILEGES ON mysql-grafana_monitoring.* TO 'user'@'localhost';

FLUSH PRIVILEGES;

USE mysql-grafana_monitoring;

CREATE TABLE system_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cpu_usage FLOAT,
    memory_usage FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 4️⃣ Update Script (If Needed)

Inside metrics_collector.py:

```
db_config = {
    "host": "localhost",
    "user": "user",
    "password": "YourPassword",
    "database": "mysql-grafana_monitoring"
}
```

### ▶️ Running the Script
Manual run:

` python3 metrics_collector.py `

### 🔁 Running Every Minute

Cron Job:

` crontab -e `

Add:

` * * * * * /usr/bin/python3 /opt/python-mysql-grafana_monitoring/metrics_collector.py >> /opt/python-mysql-grafana_monitoring/logs/metrics.log 2&>1 `

## 📊 Grafana Dashboard Setup

1️⃣ Install Grafana

2️⃣ Add MySQL as Data Source
   * Host: localhost:3306
   * Database: mysql-grafana_monitoring
   * User: user
   * Password: YourPassword

3️⃣ Create Panel with query:
```
SELECT
  created_at as time,
  cpu_usage,
  memory_usage
FROM system_metrics
ORDER BY created_at DESC
```

4️⃣ Set visualization type:
    * Time Series
    * Add two fields:
      _ CPU Usage
      _ Memory Usage

## 📄 Logging
Logs stored at:

` /opt/python-mysql-grafana_monitoring/logs/metrics.log `

Example log entry:

` 2026-02-12 10:21:01 INFO Inserted CPU=23.5 MEMORY=41.2 `

If any exception occurs, it will be logged as:

` ERROR <error_message> `

## 🎯 Real-World Use Case
This setup mimics:
* Infrastructure health monitoring
* Server performance tracking
* DevOps monitoring stack
* Lightweight alternative to Prometheus for small environments

## 📌 Why This Project Matters
This project demonstrates:
* Python automation skills
* Database integration
* Linux scheduling (cron/systemd)
* Logging best practices
* Monitoring stack integration
* DevOps workflow understanding
It reflects practical real-world monitoring implementation.
