import pandas as pd


class Analytics:

    @staticmethod
    def calculate_farm_health(df):

        latest = df.iloc[-1]

        score = 100

        if latest["soil_moisture"] < 30:
            score -= 25

        if latest["temperature"] > 38:
            score -= 25

        if latest["water_level"] < 20:
            score -= 25

        if latest["humidity"] < 40:
            score -= 25

        return max(score, 0)