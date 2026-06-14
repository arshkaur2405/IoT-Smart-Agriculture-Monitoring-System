# 🌾 IoT-Enabled Smart Agriculture Monitoring System

## 📌 Project Overview

The IoT-Enabled Smart Agriculture Monitoring System is a virtual smart farming solution developed using Python and Streamlit. The project simulates real-world agricultural sensors and provides automated irrigation decisions, smart alerts, real-time monitoring, and farm analytics through an interactive dashboard.

This project demonstrates how Internet of Things (IoT) technologies can improve farming efficiency, reduce water wastage, and support data-driven agricultural decision-making without requiring physical hardware.

---

## 🎯 Problem Statement

Traditional farming often relies on manual monitoring of soil and environmental conditions, which can lead to:

* Water wastage
* Over-irrigation
* Under-irrigation
* Delayed response to crop stress
* Increased labor requirements

This project solves these challenges by continuously monitoring simulated sensor values and providing automated recommendations and irrigation decisions.

---

## 🚀 Features

### 🌱 Virtual Sensor Simulation

* Soil Moisture Sensor
* Temperature Sensor
* Humidity Sensor
* Light Intensity Sensor
* Water Level Sensor

### ⚙ Automated Irrigation Logic

* Pump ON/OFF simulation
* Soil moisture threshold monitoring
* Smart irrigation decisions

### 🚨 Smart Alert System

* Low Soil Moisture Alert
* High Temperature Alert
* Low Water Tank Alert
* Farm Health Monitoring

### 📊 Real-Time Dashboard

* Live Sensor Metrics
* Farm Health Score
* Interactive Charts
* Alert Center
* Sensor Health Monitoring
* Downloadable Reports

### 📈 Analytics

* Average Temperature
* Average Humidity
* Average Soil Moisture
* Water Level Monitoring
* Historical Trend Analysis

### 💾 Data Management

* CSV Data Logging
* Rolling Storage Buffer
* Maximum 1000 Records Retained
* Automatic Old Record Removal

---

## 🏗 System Architecture

```text
Virtual Sensors
       │
       ▼
Sensor Simulator
       │
       ▼
Decision Engine
       │
       ▼
Threshold Analysis
       │
       ▼
Alert Generation
       │
       ▼
Irrigation Controller
       │
       ▼
CSV Data Logger
       │
       ▼
Streamlit Dashboard
       │
       ▼
Analytics & Reports
```

---

## 📂 Project Structure

```text
IoT-Smart-Agriculture-Monitoring-System/

│
├── app.py
│
├── src/
│   ├── __init__.py
│   ├── sensor_simulator.py
│   ├── irrigation_controller.py
│   ├── alert_engine.py
│   ├── data_logger.py
│   ├── analytics.py
│   └── recommendations.py
│
├── dashboard/
│   └── dashboard.py
│
├── data/
│   └── agriculture_data.csv
│
├── images/
│
├── docs/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠 Technologies Used

### Programming Language

* Python

### Dashboard Framework

* Streamlit

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly

### Storage

* CSV File System

### IoT Concepts

* Sensor Simulation
* Data Acquisition
* Threshold Monitoring
* Alert Generation
* Automated Irrigation Logic

---

## 📥 Installation

### Clone Repository

```bash
git clone https://github.com/arshkaur2405/IoT-Smart-Agriculture-Monitoring-System.git
```

```bash
cd IoT-Smart-Agriculture-Monitoring-System
```

---

### Create Virtual Environment

#### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

### Step 1: Start Sensor Simulation

```bash
python app.py
```

This continuously generates virtual sensor readings and stores them in a CSV file.

---

### Step 2: Launch Dashboard

Open a new terminal and activate the virtual environment.

Run:

```bash
streamlit run dashboard/dashboard.py
```

Dashboard opens automatically at:

```text
http://localhost:8501
```

---

## 📊 Dashboard Modules

### Farm Health Score

Evaluates overall farm condition using sensor thresholds.

### Live Metrics

* Soil Moisture
* Temperature
* Humidity
* Light Intensity
* Water Level

### Alert Center

Displays active farm alerts.

### Analytics Section

Provides averages and trend analysis.

### Sensor Health Table

Shows operational status of all virtual sensors.

### Report Download

Allows CSV export of recorded sensor data.

---

## 🚨 Alert Conditions

| Condition            | Trigger |
| -------------------- | ------- |
| Low Soil Moisture    | < 30%   |
| High Temperature     | > 38°C  |
| Low Water Tank Level | < 20%   |
| Low Humidity         | < 40%   |

---

## ⚙ Automated Irrigation Logic

```python
if soil_moisture < 30:
    pump = "ON"
else:
    pump = "OFF"
```

---

## 📈 Sample Output

```text
🌱 Soil Moisture : 24 %
🌡 Temperature : 39.5 °C
💧 Humidity : 42 %
🚰 Water Level : 18 %

⚙ Pump Status : ON

🚨 Alerts:
Low Soil Moisture
High Temperature
Low Water Tank Level

💡 Recommendation:
Start irrigation immediately.
Provide shade or cooling.
Refill water tank.
```

---


## 🎓 Learning Outcomes

This project demonstrates:

* IoT System Design
* Sensor Data Processing
* Automation Logic
* Data Logging
* Dashboard Development
* Data Visualization
* Alert Management
* Smart Agriculture Concepts
* Real-Time Monitoring Systems

---

## 🔮 Future Enhancements

* Weather API Integration
* MQTT Communication
* Cloud Database Integration
* Mobile Application
* Multi-Farm Monitoring
* AI-Based Irrigation Prediction
* Crop Recommendation Engine
* Predictive Analytics
* PDF Report Generation

---

## 💼 Resume Description

Developed a virtual IoT-based Smart Agriculture Monitoring System using Python and Streamlit. Implemented real-time sensor simulation, automated irrigation control, alert management, farm health analytics, rolling data storage, and interactive dashboard visualization to demonstrate smart farming and IoT automation concepts.

---

## 👨‍💻 Author

Arshdeep Kaur

B.Tech Student | IoT Enthusiast | Python Developer | Smart Systems Learner
