class Road:
    def __init__(self, _length, _width, mass_asphalt=25, depth=5):
        self._length = _length
        self._width = _width
        self.mass_asphalt = mass_asphalt
        self.depth = depth

    def calc_mass_asphalt(self):
        return int((self._length * self._width * self.mass_asphalt * self.depth) / 1000)


a = Road(5000, 20)
print(a.calc_mass_asphalt())