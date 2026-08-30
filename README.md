# 🌋 Subsidence Monitoring System

### AI-Powered Ground Subsidence & Landslide Risk Detection with Automated Telegram Alerts

An intelligent sensor-monitoring prototype that uses **Machine Learning** to analyze ground movement and environmental conditions, estimate landslide risk, visualize sensor data, and automatically send an emergency **Telegram alert** when critical conditions are detected.

---

## 🎬 Demo

> **Watch the complete system in action — from sensor input to ML prediction, risk classification, Telegram alert, and monitoring dashboard.**

### ▶️ Demo Video


https://github.com/user-attachments/assets/c69b14af-45ea-40da-9512-b39b82dc96ba





### Demo Flow

```text
🚀 START SYSTEM
      │
      ▼
🤖 TRAIN RANDOM FOREST MODEL
      │
      ▼
📡 ENTER SENSOR READINGS
      │
      ▼
🧠 ML RISK PREDICTION
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
      │        📲 TELEGRAM ALERT
      │               │
      └───────┬───────┘
              ▼
       📈 DASHBOARD
```

The demo showcases the complete pipeline:

**Sensor Data → Machine Learning → Risk Prediction → Alert System → Visualization**

---

# 🚨 Overview

Ground subsidence and slope instability can develop before a major landslide occurs.

This project demonstrates how multiple sensor measurements can be combined with Machine Learning to create a prototype **early-warning monitoring system**.

The system monitors four parameters:

* 📐 **Tilt**
* 📳 **Vibration**
* 🧪 **Strain**
* 🌡️ **Temperature**

A **Random Forest Classifier** processes these measurements and predicts the probability of a landslide-related risk.

When the predicted probability reaches the high-risk threshold, the system automatically sends an emergency notification through Telegram.

---

# ✨ Features

| Feature                    | Description                         |
| -------------------------- | ----------------------------------- |
| 🤖 Machine Learning        | Random Forest based risk classifier |
| 📐 Tilt Monitoring         | Detects abnormal inclination        |
| 📳 Vibration Monitoring    | Detects unusual vibration levels    |
| 🧪 Strain Monitoring       | Tracks structural/ground strain     |
| 🌡️ Temperature Monitoring | Monitors environmental temperature  |
| 📊 Risk Probability        | Calculates probability from 0–100%  |
| 🚦 Risk Classification     | LOW / MEDIUM / HIGH                 |
| 🚨 Telegram Alerts         | Automatic emergency notification    |
| 💾 Model Persistence       | Saves trained model using Joblib    |
| 📈 Dashboard               | Visual sensor and risk monitoring   |
| 🧠 Feature Importance      | Shows model feature contribution    |
| 📉 Risk Trend              | Displays recent risk trend          |

---

# 🧠 System Architecture

```text
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
                     │   RISK PROBABILITY      │
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
                 │                │       ┌─────────────────┐
                 │                │       │ TELEGRAM ALERT  │
                 │                │       └─────────────────┘
                 │                │                │
                 └────────────────┴────────────────┘
                                  │
                                  ▼
                     ┌─────────────────────────┐
                     │    MONITORING DASHBOARD │
                     └─────────────────────────┘
```

---

# 📊 Sensor Parameters

The model uses four input features.

| Parameter       |   Example | Purpose                             |
| --------------- | --------: | ----------------------------------- |
| 📐 Tilt         |    `0.5°` | Detects abnormal inclination        |
| 📳 Vibration    |  `0.03 g` | Detects unusual ground vibration    |
| 🧪 Strain       | `350 ohm` | Represents structural/ground strain |
| 🌡️ Temperature |    `27°C` | Environmental condition             |

These parameters are combined and passed to the machine-learning model.

---

# 🤖 Machine Learning Model

The project uses a **Random Forest Classifier** from Scikit-learn.

```python
RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    class_weight="balanced"
)
```

### Input

```text
[Tilt, Vibration, Strain, Temperature]
```

### Output

```text
0 → NO LANDSLIDE
1 → LANDSLIDE LIKELY
```

The model also generates a probability score:

```text
0% ─────────────────────────────── 100%
```

---

# 🧪 Training Data

The current prototype generates **2,000 synthetic sensor samples** using NumPy.

The synthetic risk labels are generated using conditions such as:

```text
|Tilt| > 1.5°
```

```text
Vibration > 0.12 g
```

```text
Strain > 380
```

```text
Temperature > 32°C
AND
Vibration > 0.08 g
```

The generated data is then used to train the Random Forest model.

### Why synthetic data?

This allows the complete Machine Learning pipeline to be demonstrated without requiring a large real-world geological dataset.

> ⚠️ The current training dataset is synthetic and is intended for educational/prototype purposes.

---

# 🚦 Risk Classification

The model's probability output is converted into three risk categories.

|   Probability | Risk Level     | System Response      |
| ------------: | -------------- | -------------------- |
|       `< 30%` | 🟢 LOW RISK    | Normal monitoring    |
| `30% – < 60%` | 🟠 MEDIUM RISK | Increased monitoring |
|       `≥ 60%` | 🔴 HIGH RISK   | Telegram alert       |

---

# 🚨 Telegram Emergency Alert

The most important automation feature is the Telegram alert system.

When:

```text
Risk Probability ≥ 60%
```

the system automatically sends an emergency message.

### Example Alert

```text
🚨 LANDSLIDE ALERT 🚨

⚠️ HIGH LANDSLIDE RISK DETECTED

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
```

The alert contains both the **prediction** and the **sensor readings**, making it easier to understand why an alert was generated.

---

# 📈 Monitoring Dashboard

After prediction, the system generates a Matplotlib dashboard.

The dashboard contains four components.

### 1️⃣ Current Sensor Readings

Displays:

```text
Tilt
Vibration
Strain
Temperature
```

### 2️⃣ Landslide Probability

Displays the predicted probability from:

```text
0% → 100%
```

with threshold markers at:

```text
30% → Medium Risk
60% → High Risk
```

### 3️⃣ Feature Importance

Displays the relative importance of:

```text
Tilt
Vibration
Strain
Temperature
```

This helps visualize which inputs the Random Forest model considers important.

### 4️⃣ Recent Risk Trend

Displays the recent risk-probability trend for monitoring purposes.

---

# 🖼️ Screenshots

Add your screenshots inside the `assets` folder.

### 📊 Monitoring Dashboard

```markdown
![Monitoring Dashboard](assets/dashboard.png)
```

### 🚨 Telegram Alert

```markdown
![Telegram Alert](assets/telegram-alert.png)
```

Recommended structure:

```text
assets/
├── dashboard.png
└── telegram-alert.png
```

---

# 🧪 Example Test Cases

## 🟢 Low Risk

Example sensor readings:

```text
Tilt:          0.3°
Vibration:     0.02 g
Strain:        345 ohm
Temperature:   27°C
```

Expected behavior:

```text
LOW RISK
```

No Telegram alert is sent.

---

## 🟠 Medium Risk

Example readings:

```text
Tilt:          1.2°
Vibration:     0.08 g
Strain:        365 ohm
Temperature:   30°C
```

Expected behavior:

```text
MEDIUM RISK
```

No emergency alert is triggered.

---

## 🔴 High Risk

Example readings:

```text
Tilt:          2.1°
Vibration:     0.15 g
Strain:        395 ohm
Temperature:   34°C
```

Expected behavior:

```text
HIGH RISK
```

The system attempts to send:

```text
🚨 LANDSLIDE ALERT 🚨
```

to the configured Telegram chat.

> These are example test inputs. The exact probability produced by the model may vary.

---

# 🛠️ Technology Stack

```text
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
                 │ Requests  │
                 │ Telegram  │
                 └───────────┘
```

### Libraries

* **NumPy** — numerical computation and synthetic sensor data
* **Scikit-learn** — Random Forest machine learning
* **Matplotlib** — visualization and dashboard
* **Joblib** — model persistence
* **Requests** — Telegram Bot API communication
* **Datetime** — timestamps

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/prabuddha34/SubsidenceMonitoringSystem.git
```

Navigate to the project:

```bash
cd SubsidenceMonitoringSystem
```

Install dependencies:

```bash
pip install numpy matplotlib scikit-learn joblib requests
```

Or create a `requirements.txt`:

```text
numpy
matplotlib
scikit-learn
joblib
requests
```

Then:

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Run the main program:

```bash
python main.py
```

The program will ask for current sensor values:

```text
==============================================
ENTER CURRENT SENSOR VALUES
==============================================

Tilt X (degrees) [example 0.5]:
Vibration (g) [example 0.03]:
Strain (ohm) [example 350]:
Temperature (°C) [example 27]:
```

The system then performs:

```text
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
```

---

# 📁 Project Structure

```text
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
│   └── landslide-demo.mp4
│
└── landslide_sensor_model.pkl
```

---

# 🔐 Security

## Protect your Telegram credentials

**Never commit your Telegram bot token to GitHub.**

Instead of hardcoding credentials:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
```

use environment variables:

```python
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
```

### Windows PowerShell

```powershell
$env:TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
$env:TELEGRAM_CHAT_ID="YOUR_CHAT_ID"
```

### `.gitignore`

Add:

```text
.env
*.pkl
__pycache__/
```

If a real Telegram bot token has already been exposed publicly, **regenerate/revoke it before publishing the repository**.

---

# 🔮 Future Improvements

The prototype can be expanded into a complete IoT-based landslide monitoring platform.

## 🔌 Hardware Integration

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

## 📡 Real-Time Monitoring

Future architecture:

```text
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
```

---

## 🌐 Web Dashboard

Future versions could include:

* Real-time graphs
* Historical sensor data
* Multiple monitoring locations
* GPS coordinates
* Sensor status
* Risk maps
* Alert history

---

## 🤖 Advanced ML

The current Random Forest model could be compared with:

```text
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
```

Future models could use historical sequences of sensor measurements rather than a single reading.

---

# 🎯 Project Goals

The project demonstrates the integration of five major concepts:

```text
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
       EARLY WARNING
```

The main goal is to demonstrate how Machine Learning can be integrated with sensor monitoring and automated communication to create an early-warning prototype.

---

# ⚠️ Disclaimer

This project is an **educational and experimental prototype**.

The current model uses synthetically generated training data and simplified risk rules. It should **not be used as an actual geological emergency warning system**.

A real deployment would require:

* Real-world sensor data
* Geological datasets
* Sensor calibration
* Field testing
* Model validation
* False-positive/false-negative analysis
* Geological expert evaluation
* Long-term monitoring
* Independent safety validation

---

# 👨‍💻 Author

## Prabuddha Pal

Computer Science & Engineering Student

### Interests

```text
🤖 Machine Learning
🔌 IoT
🔐 Cybersecurity
💻 Software Development
🏆 Competitive Programming
```

### GitHub

**[@prabuddha34](https://github.com/prabuddha34)**

---

# ⭐ Support

If you found this project interesting, consider giving the repository a ⭐.

Contributions, improvements, and ideas are welcome.

---

<div align="center">

### 🌋 Predict • Monitor • Analyze • Alert

**Built with Python + Machine Learning + Sensor Analytics + Telegram Automation**

</div>
