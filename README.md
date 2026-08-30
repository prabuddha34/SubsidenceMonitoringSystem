# 🌋 Subsidence Monitoring System

### AI-Powered Ground Subsidence & Landslide Risk Detection with Telegram Alerts

An intelligent **sensor-based monitoring system** that uses Machine Learning to analyze ground movement and environmental conditions, estimate the probability of a landslide/subsidence event, and automatically send an emergency **Telegram alert** when dangerous conditions are detected.

---

## 🚨 Project Overview

Ground subsidence and slope instability can develop gradually before becoming a major hazard.

This project demonstrates a prototype early-warning system that combines:

**Sensor Data + Machine Learning + Risk Analysis + Visualization + Automated Alerts**

The system takes four sensor readings:

* 📐 **Tilt**
* 📳 **Vibration**
* 🧪 **Strain**
* 🌡️ **Temperature**

A **Random Forest Classifier** analyzes these measurements and produces a probability-based risk assessment.

If the predicted risk reaches the critical threshold, the system automatically sends an alert through **Telegram**.

---

## ⚡ Key Features

* 🤖 **Random Forest Machine Learning**
* 📡 Multi-sensor monitoring
* 📊 Probability-based risk prediction
* 🚦 LOW / MEDIUM / HIGH risk classification
* 🚨 Automatic Telegram emergency alerts
* 💾 Trained model persistence using Joblib
* 📈 Sensor monitoring dashboard
* 🧠 Feature importance visualization
* 📉 Recent risk trend visualization
* 🕐 Timestamped alerts

---

## 🧠 System Architecture

```text
                    ┌───────────────────────┐
                    │    SENSOR INPUTS      │
                    ├───────────────────────┤
                    │                       │
                    │  📐 Tilt              │
                    │  📳 Vibration         │
                    │  🧪 Strain            │
                    │  🌡️ Temperature       │
                    │                       │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   RANDOM FOREST ML    │
                    │        MODEL          │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │  RISK PROBABILITY     │
                    │       0 - 100%        │
                    └───────────┬───────────┘
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
         🟢 LOW RISK       🟠 MEDIUM RISK     🔴 HIGH RISK
             <30%             30-60%             ≥60%
                                                   │
                                                   ▼
                                      ┌─────────────────────┐
                                      │  TELEGRAM ALERT 🚨  │
                                      └─────────────────────┘
```

---

# 📊 Sensor Parameters

| Parameter       |   Example | Purpose                                     |
| --------------- | --------: | ------------------------------------------- |
| 📐 Tilt         |    `0.5°` | Detects abnormal ground/surface inclination |
| 📳 Vibration    |  `0.03 g` | Detects unusual ground vibration            |
| 🧪 Strain       | `350 ohm` | Represents structural/ground strain         |
| 🌡️ Temperature |    `27°C` | Environmental condition                     |

These measurements are combined and passed to the machine-learning model.

---

# 🤖 Machine Learning

The system uses a **Random Forest Classifier** from Scikit-learn.

```python
RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    class_weight="balanced"
)
```

The model receives four features:

```text
[Tilt, Vibration, Strain, Temperature]
```

and predicts:

```text
0 → NO LANDSLIDE
1 → LANDSLIDE LIKELY
```

The model also calculates a probability score:

```text
0% ─────────────────────────────── 100%
```

---

# 🧪 Training Data

The current prototype generates **2,000 synthetic sensor samples** using NumPy.

Risk conditions are simulated using combinations of sensor thresholds such as:

```text
|Tilt| > 1.5°
Vibration > 0.12 g
Strain > 380
Temperature > 32°C + elevated vibration
```

The generated dataset is then used to train the Random Forest model.

### Why synthetic data?

The prototype is designed to demonstrate the complete pipeline without requiring a large real-world geological dataset.

> ⚠️ The current model is **not a scientifically validated geological prediction model**. Real-world deployment would require properly collected and labeled sensor data.

---

# 🚦 Risk Classification

The predicted probability is converted into three risk levels:

|   Probability | Level          | Action               |
| ------------: | -------------- | -------------------- |
|       `< 30%` | 🟢 LOW RISK    | Normal monitoring    |
| `30% – < 60%` | 🟠 MEDIUM RISK | Increased monitoring |
|       `≥ 60%` | 🔴 HIGH RISK   | Telegram alert       |

---

# 🚨 Telegram Emergency Alert

When the probability reaches **60% or above**, the system automatically sends a Telegram alert.

Example:

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
34°C

━━━━━━━━━━━━━━━━━━━━

🕐 Time:
2026-08-30 23:30:00

⚠️ Immediate attention required.
```

This makes the project more than just an ML prediction system — it demonstrates an **automated monitoring → prediction → emergency notification pipeline**.

---

# 📈 Monitoring Dashboard

The system generates a visual dashboard using Matplotlib.

### Dashboard components

**1. Current Sensor Readings**

Displays the current readings from all four sensors.

**2. Landslide Probability**

Displays the model's predicted probability from 0–100%.

**3. Model Feature Importance**

Shows which sensor parameters contribute most to the Random Forest's decisions.

**4. Recent Risk Trend**

Displays a recent risk-probability trend for monitoring purposes.

---

# 🛠️ Technologies Used

```text
Python
│
├── NumPy
│   └── Sensor data generation
│
├── Scikit-learn
│   └── Random Forest Classifier
│
├── Joblib
│   └── Model saving
│
├── Requests
│   └── Telegram Bot API
│
├── Matplotlib
│   └── Data visualization
│
└── Datetime
    └── Alert timestamps
```

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/prabuddha34/SubsidenceMonitoringSystem.git
```

Enter the project directory:

```bash
cd SubsidenceMonitoringSystem
```

Install dependencies:

```bash
pip install numpy matplotlib scikit-learn joblib requests
```

---

# ▶️ Running the System

Run:

```bash
python main.py
```

The program will request the current sensor values:

```text
==============================================
ENTER CURRENT SENSOR VALUES
==============================================

Tilt X (degrees) [example 0.5]:
Vibration (g) [example 0.03]:
Strain (ohm) [example 350]:
Temperature (°C) [example 27]:
```

The system then:

```text
1. Generates training data
        ↓
2. Trains Random Forest
        ↓
3. Saves the ML model
        ↓
4. Reads current sensor values
        ↓
5. Calculates risk probability
        ↓
6. Determines risk level
        ↓
7. Sends Telegram alert if HIGH RISK
        ↓
8. Displays monitoring dashboard
```

---

# 📁 Repository Structure

```text
SubsidenceMonitoringSystem/
│
├── main.py
│
├── README.md
│
└── landslide_sensor_model.pkl
```

---

# 🔐 Security

### ⚠️ Protect your Telegram credentials

Never commit your bot token directly to GitHub.

Use environment variables instead:

```python
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
```

For Windows PowerShell:

```powershell
$env:TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
$env:TELEGRAM_CHAT_ID="YOUR_CHAT_ID"
```

### 🚨 Important

If the Telegram bot token currently present in your `main.py` is a real active token, **regenerate it immediately using BotFather** before keeping the repository public.

---

# 🔮 Future Improvements

The current system can be developed into a real IoT-based monitoring platform.

### 🔌 Hardware Integration

* ESP32
* Arduino
* MPU6050
* Tilt sensors
* Vibration sensors
* Strain gauges
* Temperature sensors
* Soil-moisture sensors
* Rainfall sensors

### ☁️ Cloud Integration

```text
Sensors
   ↓
ESP32
   ↓
Internet
   ↓
Cloud Server
   ↓
ML Model
   ↓
Dashboard + Telegram
```

### 🧠 Advanced Machine Learning

Future versions could compare:

* Random Forest
* XGBoost
* Gradient Boosting
* SVM
* LSTM
* Time-series models

with real historical sensor measurements.

### 🌐 Additional Features

* Live web dashboard
* GPS-based monitoring
* Historical data storage
* Multiple monitoring locations
* Mobile notifications
* SMS/WhatsApp alerts
* Rainfall integration
* Soil moisture monitoring
* Long-term trend analysis

---

# 🎯 Project Objective

The primary objective is to demonstrate how **Machine Learning can be combined with sensor monitoring and automated communication systems** to create an early-warning prototype for ground instability.

```text
        SENSOR DATA
             │
             ▼
      MACHINE LEARNING
             │
             ▼
       RISK ANALYSIS
             │
       ┌─────┴─────┐
       ▼           ▼
   MONITOR      ALERT 🚨
       │           │
       └─────┬─────┘
             ▼
       EARLY WARNING
```

---

# ⚠️ Disclaimer

This project is an **educational and experimental prototype**.

The training data is synthetically generated and the risk thresholds are simplified. The system should **not be used as an actual geological emergency warning system**.

A production system would require:

* Real-world sensor data
* Geological datasets
* Sensor calibration
* Field testing
* Model validation
* False-positive/false-negative analysis
* Geological expert evaluation
* Safety and reliability testing

---

# 👨‍💻 Author

## Prabuddha Pal

Computer Science & Engineering Student

**Interests:**

```text
Machine Learning
IoT
Cybersecurity
Software Development
Competitive Programming
```

---

### 🌋 Predict • Monitor • Analyze • Alert

**Built with Python, Machine Learning, Sensor Analytics and Telegram Automation.**

⭐ If you find this project interesting, consider giving the repository a star.
