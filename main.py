
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import joblib
import requests
from datetime import datetime

print("==============================================")
print("LANDSLIDE RISK SYSTEM")
print("==============================================")

BOT_TOKEN = "8736792125:AAHaXAF8jAXj2eHZ4W6mxNPF2jSDfZ-jAGs"
CHAT_ID = "5857153902"

print("\nCreating training data...")

np.random.seed(42)

n_samples = 2000

tilt = np.random.normal(
    0,
    0.8,
    n_samples
)

vibration = np.abs(
    np.random.normal(
        0.02,
        0.04,
        n_samples
    )
)

strain = np.random.normal(
    350,
    15,
    n_samples
)

temperature = np.random.normal(
    26,
    4,
    n_samples
)

risk = (
        (np.abs(tilt) > 1.5) |
        (vibration > 0.12) |
        (strain > 380) |
        ((temperature > 32) & (vibration > 0.08))
).astype(int)

X = np.column_stack([
    tilt,
    vibration,
    strain,
    temperature
])

y = risk

print("Training samples:", n_samples)

print("\nTraining Random Forest model...")

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    class_weight="balanced"
)

model.fit(X, y)

joblib.dump(
    model,
    "landslide_sensor_model.pkl"
)

print("Model trained successfully!")
print("Model saved as landslide_sensor_model.pkl")


def send_telegram_alert(
        probability,
        tilt_x,
        vibration_value,
        strain_value,
        temperature_value
):

    message = f"""
🚨 LANDSLIDE ALERT 🚨

⚠️ HIGH LANDSLIDE RISK DETECTED

━━━━━━━━━━━━━━━━━━━━

📊 Risk Probability:
{probability * 100:.1f}%

🌋 Risk Level:
HIGH RISK

━━━━━━━━━━━━━━━━━━━━

📡 SENSOR READINGS

Tilt:
{tilt_x}°

Vibration:
{vibration_value} g

Strain:
{strain_value} ohm


━━━━━━━━━━━━━━━━━━━━

🕐 Time:
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

⚠️ Immediate attention required.
"""

    url = (
        f"https://api.telegram.org/"
        f"bot{BOT_TOKEN}/sendMessage"
    )

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:

        response = requests.post(
            url,
            data=data,
            timeout=10
        )

        if response.status_code == 200:

            print("\n==============================================")
            print("TELEGRAM ALERT SENT SUCCESSFULLY")
            print("==============================================")

        else:

            print("\n==============================================")
            print("TELEGRAM ALERT FAILED")
            print("==============================================")

            print(
                "Telegram response:",
                response.text
            )

    except Exception as e:

        print("\n==============================================")
        print("TELEGRAM CONNECTION FAILED")
        print("==============================================")

        print(
            "Error:",
            e
        )


def get_float(prompt):

    while True:

        try:

            value = input(prompt).strip()

            return float(value)

        except ValueError:

            print(
                "❌ Please enter a valid number."
            )


print("\n==============================================")
print("ENTER CURRENT SENSOR VALUES")
print("==============================================")

tilt_x = get_float(
    "Tilt X (degrees) [example 0.5]: "
)

vibration_value = get_float(
    "Vibration (g) [example 0.03]: "
)

strain_value = get_float(
    "Strain (ohm) [example 350]: "
)

temperature_value = get_float(
    "Temperature (°C) [example 27]: "
)


features = np.array([
    [
        tilt_x,
        vibration_value,
        strain_value,
        temperature_value
    ]
])


probability = model.predict_proba(
    features
)[0][1]

prediction = model.predict(
    features
)[0]


if probability < 0.30:

    level = "LOW RISK"
    risk_color = "green"

elif probability < 0.60:

    level = "MEDIUM RISK"
    risk_color = "orange"

else:

    level = "HIGH RISK"
    risk_color = "red"


print("\n==============================================")
print("PREDICTION RESULT")
print("==============================================")

print(
    f"Landslide Probability : "
    f"{probability * 100:.1f}%"
)

print(
    f"Risk Level            : "
    f"{level}"
)

print(
    "Binary Prediction     : "
    +
    (
        "LANDSLIDE LIKELY"
        if prediction == 1
        else "NO LANDSLIDE"
    )
)

print("\nSensor Values:")

print(
    f"Tilt          : {tilt_x}°"
)

print(
    f"Vibration     : {vibration_value} g"
)

print(
    f"Strain        : {strain_value} ohm"
)

print(
    f"Temperature   : {temperature_value} °C"
)


if probability >= 0.60:

    print("\n!!! HIGH RISK DETECTED !!!")

    print(
        "!!! SENDING TELEGRAM ALERT !!!"
    )

    send_telegram_alert(
        probability,
        tilt_x,
        vibration_value,
        strain_value,
        temperature_value
    )

else:

    print("\nNo Telegram alert sent.")

    print(
        "Risk is not high enough."
    )


fig, axes = plt.subplots(
    2,
    2,
    figsize=(12, 9)
)

fig.suptitle(
    "Landslide Sensor Dashboard",
    fontsize=16,
    fontweight="bold"
)


labels = [
    "Tilt (°)",
    "Vibration (g)",
    "Strain (ohm)",
    "Temp (°C)"
]

values = [
    tilt_x,
    vibration_value,
    strain_value,
    temperature_value
]


axes[0, 0].bar(
    labels,
    values
)

axes[0, 0].set_title(
    "Current Sensor Readings"
)

axes[0, 0].tick_params(
    axis="x",
    rotation=15
)


axes[0, 1].barh(
    ["Risk"],
    [probability]
)

axes[0, 1].set_xlim(
    0,
    1
)

axes[0, 1].set_title(
    f"Landslide Probability: "
    f"{probability * 100:.1f}%"
)

axes[0, 1].axvline(
    0.30,
    linestyle="--",
    label="Low"
)

axes[0, 1].axvline(
    0.60,
    linestyle="--",
    label="High"
)

axes[0, 1].legend()


importances = model.feature_importances_

axes[1, 0].barh(
    labels,
    importances
)

axes[1, 0].set_title(
    "What the Model Pays Attention To"
)

axes[1, 0].set_xlabel(
    "Importance"
)


history = np.clip(
    np.random.normal(
        probability,
        0.08,
        20
    ),
    0,
    1
)

axes[1, 1].plot(
    history,
    marker="o"
)

axes[1, 1].axhline(
    0.60,
    linestyle="--",
    alpha=0.7
)

axes[1, 1].set_title(
    "Recent Risk Trend (Simulated)"
)

axes[1, 1].set_ylabel(
    "Probability"
)

axes[1, 1].set_xlabel(
    "Last 20 readings"
)


plt.tight_layout()

plt.show()

print("\n==============================================")
print("LANDSLIDE SYSTEM FINISHED")
print("==============================================")
