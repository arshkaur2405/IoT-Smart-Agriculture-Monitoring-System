class RecommendationEngine:

    @staticmethod
    def get_recommendation(data):

        recommendations = []

        if data["soil_moisture"] < 30:
            recommendations.append(
                "Start irrigation immediately."
            )

        if data["temperature"] > 38:
            recommendations.append(
                "Provide shade or cooling."
            )

        if data["water_level"] < 20:
            recommendations.append(
                "Refill water tank."
            )

        if data["humidity"] < 40:
            recommendations.append(
                "Increase humidity levels."
            )

        if not recommendations:
            recommendations.append(
                "Farm conditions are healthy."
            )

        return " | ".join(recommendations)