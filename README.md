🌋 Subsidence Monitoring System

AI-Powered Ground Subsidence Risk Detection with Automated Telegram Alerts

An intelligent sensor-monitoring prototype that uses Machine Learning to analyze ground movement and environmental conditions, estimate subsidence risk, visualize sensor data, and automatically send an emergency Telegram alert when critical conditions are detected.

---

🎬 Demo

«Watch the complete system in action — from sensor input to ML prediction, risk classification, Telegram alert, and monitoring dashboard.»

▶️ Demo Video

https://github.com/user-attachments/assets/c69b14af-45ea-40da-9512-b39b82dc96ba

Demo Flow

🚀 START SYSTEM
      │
      ▼
🤖 TRAIN RANDOM FOREST MODEL
      │
      ▼
📡 ENTER SENSOR READINGS
      │
      ▼
🧠 ML SUBSIDENCE RISK PREDICTION
      │
      ▼
📊 CALCULATE PROBABILITY
      │
      ▼
🚦 RISK CLASSIFICATION
      │
      ├───────────────┐
      │               │
      ▼               ▼
🟢 LOW/MEDIUM      🔴 HIGH RISK
      │               │
      │               ▼
      │        📲 SUBSIDENCE ALERT
      │               │
      └───────┬───────┘
              ▼
       📈 DASHBOARD

The demo showcases the complete pipeline:

Sensor Data → Machine Learning → Subsidence Risk Prediction → Alert System → Visualization

---

🚨 Overview

Ground subsidence refers to the gradual sinking or downward movement of the ground surface. Monitoring changes in ground conditions can help identify unusual patterns that may require further investigation.

This project demonstrates how multiple sensor measurements can be combined with Machine Learning to create a prototype early-warning subsidence monitoring system.

The system monitors four parameters:

* 📐 Tilt
* 📳 Vibration
* 🧪 Strain
* 🌡️ Temperature

A Random Forest Classifier processes these measurements and estimates the probability of a subsidence-related risk condition.

When the predicted probability reaches the configured high-risk threshold, the system automatically sends an emergency notification through Telegram.

«⚠️ This is an educational prototype and does not represent a certified geological monitoring or emergency-warning system.»

---

✨ Features

Feature| Description
🤖 Machine Learning| Random Forest based risk classifier
📐 Tilt Monitoring| Detects abnormal ground inclination
📳 Vibration Monitoring| Detects unusual ground vibration
🧪 Strain Monitoring| Tracks structural/ground strain
🌡️ Temperature Monitoring| Monitors environmental temperature
📊 Risk Probability| Calculates probability from 0–100%
🚦 Risk Classification| LOW / MEDIUM / HIGH
🚨 Telegram Alerts| Automatic subsidence notification
💾 Model Persistence| Saves trained model using Joblib
📈 Dashboard| Visual sensor and risk monitoring
🧠 Feature Importance| Shows model feature contribution
📉 Risk Trend| Displays recent risk trend

---

🧠 System Architecture

                     ┌─────────────────────────┐
                     │      SENSOR INPUTS      │
                     ├─────────────────────────┤
                     │                         │
                     │  📐 Tilt                │
                     │  📳 Vibration           │
                     │  🧪 Strain              │
                     │  🌡️ Temperature         │
                     │                         │
                     └────────────┬────────────┘
                                  │
                                  ▼
                     ┌─────────────────────────┐
                     │   RANDOM FOREST MODEL  │
                     │                         │
                     │   Machine Learning      │
                     └────────────┬────────────┘
                                  │
                                  ▼
                     ┌─────────────────────────┐
                     │   SUBSIDENCE RISK       │
                     │      PROBABILITY        │
                     │        0 - 100%         │
                     └────────────┬────────────┘
                                  │
                 ┌────────────────┼────────────────┐
                 │                │                │
                 ▼                ▼                ▼
             🟢 LOW           🟠 MEDIUM         🔴 HIGH
              <30%             30-60%             ≥60%
                 │                │                │
                 │                │                ▼
                 │                │       ┌──────────────────┐
                 │                │       │ SUBSIDENCE ALERT │
                 │                │       └──────────────────┘
                 │                │                │
                 └────────────────┴────────────────┘
                                  │
                                  ▼
                     ┌─────────────────────────┐
                     │    MONITORING DASHBOARD │
                     └─────────────────────────┘

---

📊 Sensor Parameters

The model uses four input features.

Parameter| Example| Purpose
📐 Tilt| "0.5°"| Detects changes in ground inclination
📳 Vibration| "0.03 g"| Detects unusual ground vibration
🧪 Strain| "350 ohm"| Represents structural/ground strain
🌡️ Temperature| "27°C"| Environmental condition

These parameters are combined and passed to the machine-learning model to estimate the current subsidence-related risk.

---

🤖 Machine Learning Model

The project uses a Random Forest Classifier from Scikit-learn.

RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    class_weight="balanced"
)

Input

[Tilt, Vibration, Strain, Temperature]

Output

0 → NORMAL CONDITION
1 → SUBSIDENCE RISK

The model also generates a probability score:

0% ─────────────────────────────── 100%

The probability is then used to classify the current condition as LOW, MEDIUM, or HIGH risk.

---

🧪 Training Data

The current prototype generates 2,000 synthetic sensor samples using NumPy.

The synthetic risk labels are generated using conditions such as:

|Tilt| > 1.5°

Vibration > 0.12 g

Strain > 380

Temperature > 32°C
AND
Vibration > 0.08 g

The generated data is then used to train the Random Forest model.

Why synthetic data?

This allows the complete Machine Learning pipeline to be demonstrated without requiring a large real-world geological or subsidence dataset.

«⚠️ The current training dataset is synthetic and is intended for educational/prototype purposes.»

---

🚦 Risk Classification

The model's probability output is converted into three risk categories.

Probability| Risk Level| System Response
"< 30%"| 🟢 LOW RISK| Normal monitoring
"30% – < 60%"| 🟠 MEDIUM RISK| Increased monitoring
"≥ 60%"| 🔴 HIGH RISK| Telegram alert

---

🚨 Telegram Subsidence Alert

The main automation feature is the Telegram alert system.

When:

Risk Probability ≥ 60%

the system automatically sends a subsidence-risk notification.

Example Alert

🚨 SUBSIDENCE ALERT 🚨

⚠️ HIGH SUBSIDENCE RISK DETECTED

━━━━━━━━━━━━━━━━━━━━

📊 Risk Probability:
87.4%

🌋 Risk Level:
HIGH RISK

━━━━━━━━━━━━━━━━━━━━

📡 SENSOR READINGS

Tilt:
2.1°

Vibration:
0.14 g

Strain:
392 ohm

Temperature:
34 °C

━━━━━━━━━━━━━━━━━━━━

🕐 Time:
2026-08-30 23:30:00

⚠️ Immediate attention required.

The alert contains both the prediction and the sensor readings, making it easier to understand the conditions that triggered the notification.

---

📈 Monitoring Dashboard

After prediction, the system generates a Matplotlib dashboard.

The dashboard contains four components.

1️⃣ Current Sensor Readings

Displays:

Tilt
Vibration
Strain
Temperature

2️⃣ Subsidence Risk Probability

Displays the predicted probability from:

0% → 100%

with threshold markers at:

30% → Medium Risk
60% → High Risk

3️⃣ Feature Importance

Displays the relative importance of:

Tilt
Vibration
Strain
Temperature

This helps visualize which inputs the Random Forest model considers important.

4️⃣ Recent Risk Trend

Displays the recent risk-probability trend for monitoring purposes.

---

🖼️ Screenshots

Add your screenshots inside the "assets" folder.

📊 Monitoring Dashboard

![Monitoring Dashboard](assets/dashboard.png)

🚨 Telegram Alert

![Subsidence Alert](assets/telegram-alert.png)

Recommended structure:

assets/
├── dashboard.png
└── telegram-alert.png

---

🧪 Example Test Cases

🟢 Low Risk

Example sensor readings:

Tilt:          0.3°
Vibration:     0.02 g
Strain:        345 ohm
Temperature:   27°C

Expected behavior:

LOW RISK

No Telegram alert is sent.

---

🟠 Medium Risk

Example readings:

Tilt:          1.2°
Vibration:     0.08 g
Strain:        365 ohm
Temperature:   30°C

Expected behavior:

MEDIUM RISK

No emergency alert is triggered.

---

🔴 High Risk

Example readings:

Tilt:          2.1°
Vibration:     0.15 g
Strain:        395 ohm
Temperature:   34°C

Expected behavior:

HIGH RISK

The system attempts to send:

🚨 SUBSIDENCE ALERT 🚨

to the configured Telegram chat.

«These are example test inputs. The exact probability produced by the model may vary.»

---

🛠️ Technology Stack

                    PYTHON
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
      NumPy       Scikit-learn    Matplotlib
        │              │              │
        │              ▼              │
        │       Random Forest          │
        │              │              │
        └──────────────┼──────────────┘
                       │
                 ┌─────▼─────┐
                 │  Joblib   │
                 │ ML Model  │
                 └─────┬─────┘
                       │
                       ▼
                 ┌───────────┐
                 │  Requests │
                 │  Telegram │
                 └───────────┘

Libraries

* NumPy — numerical computation and synthetic sensor data
* Scikit-learn — Random Forest machine learning
* Matplotlib — visualization and dashboard
* Joblib — model persistence
* Requests — Telegram Bot API communication
* Datetime — timestamps

---

📦 Installation

Clone the repository:

git clone https://github.com/prabuddha34/SubsidenceMonitoringSystem.git

Navigate to the project:

cd SubsidenceMonitoringSystem

Install dependencies:

pip install numpy matplotlib scikit-learn joblib requests

Or create a "requirements.txt":

numpy
matplotlib
scikit-learn
joblib
requests

Then:

pip install -r requirements.txt

---

▶️ Usage

Run the main program:

python main.py

The program will ask for current sensor values:

==============================================
ENTER CURRENT SENSOR VALUES
==============================================

Tilt X (degrees) [example 0.5]:
Vibration (g) [example 0.03]:
Strain (ohm) [example 350]:
Temperature (°C) [example 27]:

The system then performs:

Generate Training Data
        ↓
Train Random Forest
        ↓
Save Model
        ↓
Read Sensor Values
        ↓
Predict Subsidence Risk
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
│
├── assets/
│   ├── dashboard.png
│   └── telegram-alert.png
│
├── demo/
│   └── subsidence-demo.mp4
│
└── subsidence_sensor_model.pkl

---

🔐 Security

Protect your Telegram credentials

Never commit your Telegram bot token to GitHub.

Instead of hardcoding credentials:

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

use environment variables:

import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

Windows PowerShell

$env:TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
$env:TELEGRAM_CHAT_ID="YOUR_CHAT_ID"

".gitignore"

Add:

.env
*.pkl
__pycache__/

If a real Telegram bot token has already been exposed publicly, regenerate/revoke it before publishing the repository.

---

🔮 Future Improvements

The prototype can be expanded into a complete IoT-based ground subsidence monitoring platform.

🔌 Hardware Integration

Possible hardware:

* ESP32
* Arduino
* MPU6050 / IMU
* Tilt sensors
* Vibration sensors
* Strain gauges
* Temperature sensors
* Soil-moisture sensors
* Rainfall sensors

---

📡 Real-Time Monitoring

Future architecture:

Physical Sensors
       │
       ▼
     ESP32
       │
       ▼
   Internet
       │
       ▼
 Cloud / Server
       │
       ▼
 ML Prediction
       │
 ┌─────┴─────┐
 ▼           ▼
Dashboard   Alerts

---

🌐 Web Dashboard

Future versions could include:

* Real-time graphs
* Historical sensor data
* Multiple monitoring locations
* GPS coordinates
* Sensor status
* Subsidence-risk maps
* Alert history
* Offline data synchronization

---

🤖 Advanced ML

The current Random Forest model could be compared with:

Random Forest
      ↓
XGBoost
      ↓
Gradient Boosting
      ↓
SVM
      ↓
LSTM
      ↓
Time-Series Models

Future models could use historical sequences of sensor measurements rather than a single reading.

This could help the system identify changes and trends in ground conditions over time.

---

🎯 Project Goals

The project demonstrates the integration of five major concepts:

       📡 SENSOR DATA
             │
             ▼
      🤖 MACHINE LEARNING
             │
             ▼
       📊 RISK ANALYSIS
             │
       ┌─────┴─────┐
       ▼           ▼
   📈 MONITOR   🚨 ALERT
       │           │
       └─────┬─────┘
             ▼
      SUBSIDENCE MONITORING

The main goal is to demonstrate how Machine Learning can be integrated with sensor monitoring and automated communication to create a prototype ground subsidence monitoring and alert system.

---

⚠️ Disclaimer

This project is an educational and experimental prototype.

The current model uses synthetically generated training data and simplified sensor-based rules. It should not be used as an actual geological emergency warning system.

A real deployment would require:

* Real-world sensor data
* Geological and geotechnical datasets
* Sensor calibration
* Field testing
* Model validation
* False-positive/false-negative analysis
* Geological expert evaluation
* Long-term monitoring
* Independent safety validation

The current system is intended to demonstrate the technical workflow of sensor monitoring → Machine Learning → risk estimation → automated alerting, rather than provide a certified prediction of actual ground subsidence.

---

👨‍💻 Author

Prabuddha Pal

Computer Science & Engineering Student

Interests

🤖 Machine Learning
🔌 IoT
🌋 Environmental Monitoring
💻 Software Development
🏆 Competitive Programming

GitHub

"@prabuddha34" (https://github.com/prabuddha34)

---

⭐ Support

If you found this project interesting, consider giving the repository a ⭐.

Contributions, improvements, and ideas are welcome.

---

<div align="center">🌋 Monitor • Analyze • Alert

Built with Python + Machine Learning + Sensor Analytics + Telegram Automation

</div>