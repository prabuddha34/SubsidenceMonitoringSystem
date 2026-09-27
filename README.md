🌋 Subsidence Monitoring System

AI-Powered Ground Subsidence Risk Detection with Automated Telegram Alerts

A Python-based prototype that combines sensor data, machine learning, risk analysis, visualization, and Telegram notifications to monitor potential ground subsidence conditions.

The system takes readings from four parameters — tilt, vibration, strain, and temperature — and uses a Random Forest classifier to estimate subsidence-related risk.

If the predicted risk crosses the configured threshold, the system automatically sends an alert through Telegram.

«⚠️ Note: This is an educational prototype. It is not a certified geological monitoring or emergency-warning system.»

---

🎬 Demo

The demo shows the complete workflow, from entering sensor readings to ML prediction, risk classification, Telegram alerting, and dashboard visualization.

▶️ Demo Video:
https://github.com/user-attachments/assets/c69b14af-45ea-40da-9512-b39b82dc96ba

Demo Flow

Sensor Input
     ↓
Generate / Load ML Model
     ↓
Random Forest Prediction
     ↓
Risk Probability
     ↓
Risk Classification
     ↓
 ┌───────────────┐
 │               │
LOW / MEDIUM    HIGH
 │               │
 │               ↓
 │        Telegram Alert
 │               │
 └───────┬───────┘
         ↓
    Monitoring Dashboard

---

📌 About the Project

Ground subsidence is the gradual sinking or downward movement of the ground surface. Detecting unusual changes in ground conditions can help identify situations that may require further investigation.

This project demonstrates a simple machine-learning-based approach where multiple sensor readings are combined to estimate a subsidence-related risk level.

The current prototype monitors:

- 📐 Tilt
- 📳 Vibration
- 🧪 Strain
- 🌡️ Temperature

The readings are passed to a Random Forest Classifier, which produces a prediction and probability score.

The probability is then converted into three risk levels:

Probability| Risk Level
"< 30%"| 🟢 LOW
"30% – < 60%"| 🟠 MEDIUM
"≥ 60%"| 🔴 HIGH

When the probability reaches 60% or higher, the system triggers a Telegram notification.

---

✨ Features

- 🤖 Random Forest based risk classification
- 📐 Ground tilt monitoring
- 📳 Vibration monitoring
- 🧪 Strain monitoring
- 🌡️ Temperature monitoring
- 📊 Risk probability calculation
- 🚦 LOW / MEDIUM / HIGH risk classification
- 🚨 Automated Telegram alerts
- 💾 Trained model persistence using Joblib
- 📈 Matplotlib monitoring dashboard
- 🧠 Feature importance visualization
- 📉 Recent risk trend visualization

---

🏗️ System Architecture

                 SENSOR INPUT
                      │
        ┌─────────────┼─────────────┐
        │             │             │
       Tilt       Vibration       Strain
        │             │             │
        └─────────────┼─────────────┘
                      │
                Temperature
                      │
                      ▼
             ┌─────────────────┐
             │  Random Forest  │
             │   Classifier    │
             └────────┬────────┘
                      │
                      ▼
             Risk Probability
                  0 - 100%
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
        LOW         MEDIUM       HIGH
       <30%        30-60%        ≥60%
          │           │           │
          │           │           ▼
          │           │     Telegram Alert
          │           │           │
          └───────────┴───────────┘
                      │
                      ▼
               Dashboard

---

📊 Sensor Parameters

The model currently uses four features:

Parameter| Example| Purpose
Tilt| "0.5°"| Detects changes in ground inclination
Vibration| "0.03 g"| Detects unusual ground vibration
Strain| "350 Ω"| Represents structural/ground strain
Temperature| "27°C"| Provides environmental information

These values are combined and passed to the trained model for risk estimation.

---

🤖 Machine Learning

The project uses the "RandomForestClassifier" from Scikit-learn.

RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    class_weight="balanced"
)

Model Input

[Tilt, Vibration, Strain, Temperature]

Model Output

0 → NORMAL CONDITION
1 → SUBSIDENCE RISK

The model also provides a probability score which is used by the application to determine the final risk level.

---

🧪 Training Data

The current version uses 2,000 synthetically generated sensor samples created with NumPy.

The synthetic labels are generated using simplified conditions such as:

Tilt > 1.5°
Vibration > 0.12 g
Strain > 380
Temperature > 32°C AND Vibration > 0.08 g

The generated data is then used to train the Random Forest model.

Why synthetic data?

Real geological and subsidence datasets can be difficult to obtain for a small prototype.

Synthetic data makes it possible to demonstrate the complete pipeline:

Sensor Data
     ↓
Data Generation
     ↓
Model Training
     ↓
Prediction
     ↓
Risk Analysis
     ↓
Alert

«⚠️ The synthetic dataset is only intended for demonstrating the ML pipeline. It should not be treated as real geological training data.»

---

🚦 Risk Classification

The predicted probability is converted into three categories.

Probability| Level| System Response
"< 30%"| 🟢 LOW| Normal monitoring
"30% – < 60%"| 🟠 MEDIUM| Increased monitoring
"≥ 60%"| 🔴 HIGH| Telegram alert

---

🚨 Telegram Alerts

Telegram is used to notify the user when a high-risk condition is detected.

An alert is triggered when:

Risk Probability >= 60%

Example:

🚨 SUBSIDENCE ALERT 🚨

⚠️ HIGH SUBSIDENCE RISK DETECTED

Risk Probability: 87.4%
Risk Level: HIGH

SENSOR READINGS

Tilt: 2.1°
Vibration: 0.14 g
Strain: 392 Ω
Temperature: 34°C

Time: 2026-08-30 23:30:00

⚠️ Immediate attention required.

The alert includes both the prediction and the sensor readings that were used for the prediction.

---

📈 Monitoring Dashboard

The application generates a Matplotlib-based dashboard after prediction.

The dashboard displays:

Current Sensor Readings

- Tilt
- Vibration
- Strain
- Temperature

Risk Probability

The current prediction is displayed on a "0–100%" scale with the configured risk thresholds.

Feature Importance

The Random Forest feature importance values are displayed for:

Tilt
Vibration
Strain
Temperature

This provides a simple way to see which features contributed more to the trained model.

Risk Trend

Recent probability values are displayed to visualize how the estimated risk changes over time.

---

🛠️ Tech Stack

Python
 │
 ├── NumPy
 │
 ├── Scikit-learn
 │      └── Random Forest
 │
 ├── Matplotlib
 │
 ├── Joblib
 │      └── Model Persistence
 │
 └── Requests
        └── Telegram Bot API

Libraries

Library| Purpose
NumPy| Synthetic sensor data generation
Scikit-learn| Machine learning
Matplotlib| Dashboard and visualization
Joblib| Saving/loading trained model
Requests| Telegram API communication
Datetime| Timestamp generation

---

📦 Installation

1. Clone the repository

git clone https://github.com/prabuddha34/SubsidenceMonitoringSystem.git

2. Enter the project directory

cd SubsidenceMonitoringSystem

3. Install dependencies

pip install numpy matplotlib scikit-learn joblib requests

Or install from "requirements.txt":

pip install -r requirements.txt

---

▶️ Running the Project

Run:

python main.py

The program will ask for the current sensor readings:

==============================================
        ENTER CURRENT SENSOR VALUES
==============================================

Tilt X (degrees) [example 0.5]:
Vibration (g) [example 0.03]:
Strain (ohm) [example 350]:
Temperature (°C) [example 27]:

The application then performs the following steps:

Generate Training Data
        ↓
Train Random Forest
        ↓
Save Model
        ↓
Read Sensor Values
        ↓
Predict Risk
        ↓
Calculate Probability
        ↓
Classify Risk
        ↓
Send Telegram Alert
        ↓
Display Dashboard

---

📁 Project Structure

SubsidenceMonitoringSystem/
│
├── main.py
├── README.md
├── requirements.txt
│
├── demo/
│   └── subsidence-demo.mp4
│
└── subsidence_sensor_model.pkl

---

🔐 Telegram Configuration

Telegram credentials should never be hardcoded or committed to GitHub.

Instead of:

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

use environment variables:

import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

Windows PowerShell

$env:TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
$env:TELEGRAM_CHAT_ID="YOUR_CHAT_ID"

A ".gitignore" file should include:

.env
*.pkl
__pycache__/

If a real Telegram bot token is accidentally exposed, revoke/regenerate it before continuing to use the repository.

---

🧪 Example Test Cases

🟢 Low Risk

Tilt:          0.3°
Vibration:     0.02 g
Strain:        345 Ω
Temperature:   27°C

Expected:

LOW RISK

No Telegram alert is triggered.

---

🟠 Medium Risk

Tilt:          1.2°
Vibration:     0.08 g
Strain:        365 Ω
Temperature:   30°C

Expected:

MEDIUM RISK

No emergency alert is triggered.

---

🔴 High Risk

Tilt:          2.1°
Vibration:     0.15 g
Strain:        395 Ω
Temperature:   34°C

Expected:

HIGH RISK

→ Telegram alert

«The exact probability can vary because it is generated by the trained model.»

---

🔮 Future Improvements

The current project is designed as a starting point for a larger IoT-based monitoring system.

🔌 Hardware Integration

Possible hardware:

- ESP32
- Arduino
- MPU6050 / IMU
- Tilt sensors
- Vibration sensors
- Strain gauges
- Temperature sensors
- Soil-moisture sensors
- Rainfall sensors

A possible future architecture:

Physical Sensors
       ↓
     ESP32
       ↓
   Internet
       ↓
 Cloud / Server
       ↓
 ML Prediction
       ↓
 ┌─────┴─────┐
 ↓           ↓
Dashboard   Alerts

🌐 Web Dashboard

Future versions could include:

- Real-time sensor graphs
- Historical readings
- Multiple monitoring locations
- GPS coordinates
- Sensor health/status
- Risk maps
- Alert history
- Offline data synchronization

🤖 Improved Machine Learning

The current Random Forest model could later be compared with models such as:

Random Forest
      ↓
Gradient Boosting
      ↓
XGBoost
      ↓
SVM
      ↓
LSTM
      ↓
Time-Series Models

Instead of using only the current sensor reading, future versions could analyze historical sensor sequences to detect trends and changes over time.

---

🎯 Project Objective

The main objective of this project is to demonstrate how different technologies can work together in a single monitoring pipeline:

        SENSOR DATA
             ↓
     MACHINE LEARNING
             ↓
       RISK ANALYSIS
             ↓
      ┌──────┴──────┐
      ↓             ↓
 VISUALIZATION    ALERT
      │             │
      └──────┬──────┘
             ↓
      MONITORING SYSTEM

The project combines:

- Sensor analytics
- Machine learning
- Risk classification
- Data visualization
- Automated communication

into one prototype system.

---

⚠️ Disclaimer

This project is an educational and experimental prototype.

The current model uses synthetic training data and simplified rules. It is not suitable for real-world geological monitoring or emergency decision-making.

A real deployment would require:

- Real geological and geotechnical datasets
- Calibrated sensors
- Field testing
- Model validation
- False-positive/false-negative analysis
- Long-term monitoring
- Geological and geotechnical expert evaluation
- Independent safety validation

The purpose of this project is to demonstrate the technical workflow:

Sensor Monitoring
       ↓
Machine Learning
       ↓
Risk Estimation
       ↓
Automated Alert
       ↓
Visualization

---

👨‍💻 Author

Prabuddha Pal

Computer Science & Engineering Student


GitHub:
https://github.com/prabuddha34

---

⭐ Support

If you found the project interesting, consider giving the repository a ⭐.

Suggestions, improvements, and contributions are welcome.

---

<div align="center">🌋 Monitor • Analyze • Alert

Built with Python + Machine Learning + Sensor Analytics + Telegram Automation

</div>