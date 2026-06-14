import random
from datetime import datetime


class SensorSimulator:

    @staticmethod
    def generate_data():

        return {
            "timestamp": datetime.now(),

            "soil_moisture": random.randint(15, 95),

            "temperature": round(random.uniform(20, 45), 1),

            "humidity": round(random.uniform(35, 90), 1),

            "light_intensity": random.randint(200, 1200),

            "water_level": random.randint(10, 100)
        }