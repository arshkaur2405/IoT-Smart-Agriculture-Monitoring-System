class AlertEngine:

    @staticmethod
    def generate_alerts(data):

        alerts = []

        if data["soil_moisture"] < 30:
            alerts.append("Low Soil Moisture")

        if data["temperature"] > 38:
            alerts.append("High Temperature")

        if data["water_level"] < 20:
            alerts.append("Low Water Tank Level")

        if data["humidity"] < 40:
            alerts.append("Low Humidity")

        if not alerts:
            alerts.append("Normal")

        return alerts
    # ..