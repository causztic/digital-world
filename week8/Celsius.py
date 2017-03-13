class Celsius(object):

    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return float(self._temperature) * 1.8 + 32

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            value = -273
        self._temperature = value

    # temperature = property(get_temperature, set_temperature)