# by Kami Bigdely
# Docstrings and blank lines
class OnBoardTemperatureSensor:
    """Construct a tempurtature sensor.
        Have it read the voltage
        Have it get tempurature by converting voltage
    """
    VOLTAGE_TO_TEMP_FACTOR = 5.6
    def __init__(self):
        """intitize onboardtemperaturesenor"""
        pass
    def read_voltage(self):
        """returns voltage"""        
        return 2.7
    def get_temperature(self):
        """returns tempurature based on voltz"""
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]
class CarbonMonoxideSensor:
    """
    Construct a carbon Monoxide sensor
    Have is read the barbon monoxide level
    have it read the sensor voltage
    """
    VOLTAGE_TO_CO_FACTOR = 0.048
    def __init__(self, temperature_sensor):
        """initialize carbonMonoxideSensor"""
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()
    def get_carbon_monoxide_level(self):
        """extracts the carbon monoxide level from the sensors reading"""
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(self, sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide
    def read_sensor_voltage(self):
        """reads the voltage from the sensor"""
        # In real life, it should read from hardware.        
        return 2.3
    def convert_voltage_to_carbon_monoxide_level(self, voltage, temperature):
        """converts the voltage to a carbon level using an equasion"""
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature
class DisplayUnit:
    def __init__(self):
        self.string = ''
    def display(self,msg):
        print(msg)
class CarbonMonoxideDevice():
    """COnstruct a ccarbon monoxide CarbonMonoxideDevice
        have it display teh carbon monoxide level
    """
    def __init__(self, co_sensor, display_unit):
        """initialize a carbonMonoxideSensor"""
        self.carbonMonoxideSensor = co_sensor 
        self.display_unit = display_unit       
    def Display(self):
        """display the reading from the carbon monoxide"""
        msg = 'Carbon Monoxide Level is : ' +  str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)
if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.Display()