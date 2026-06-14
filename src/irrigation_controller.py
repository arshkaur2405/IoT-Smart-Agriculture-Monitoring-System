class IrrigationController:

    @staticmethod
    def get_pump_status(soil_moisture):

        if soil_moisture < 30:
            return "ON"

        return "OFF"
    # ...