class Celsius(object):

    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return float(self._temperature) * 1.8 + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            value = -273
        self._temperature = value

    #@property
    #def temperature(self)
    #@temperature.setter
    #def temperature(self, value)

    temperature = property(get_temperature, set_temperature)

c = Celsius(-500)
print c.temperature