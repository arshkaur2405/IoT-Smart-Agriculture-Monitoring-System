import time

from src.sensor_simulator import SensorSimulator
from src.irrigation_controller import IrrigationController
from src.alert_engine import AlertEngine
from src.data_logger import DataLogger
from src.recommendations import RecommendationEngine

while True:

    data = SensorSimulator.generate_data()

    data["pump_status"] = (
        IrrigationController.get_pump_status(
            data["soil_moisture"]
        )
    )

    alerts = AlertEngine.generate_alerts(data)

    data["alerts"] = ",".join(alerts)

    data["recommendation"] = (
        RecommendationEngine.get_recommendation(data)
    )

    DataLogger.save_data(data)

    print("\n" + "=" * 60)
    print("🌾 SMART AGRICULTURE MONITORING SYSTEM")
    print("=" * 60)

    print(f"🕒 Timestamp       : {data['timestamp']}")
    print(f"🌱 Soil Moisture   : {data['soil_moisture']} %")
    print(f"🌡️ Temperature    : {data['temperature']} °C")
    print(f"💧 Humidity        : {data['humidity']} %")
    print(f"☀️ Light Intensity : {data['light_intensity']} lux")
    print(f"🚰 Water Level     : {data['water_level']} %")
    print(f"⚙️ Pump Status     : {data['pump_status']}")
    print(f"🚨 Alerts          : {data['alerts']}")
    print(f"💡 Recommendation  : {data['recommendation']}")

    print("=" * 60)

    time.sleep(5)
    # ...