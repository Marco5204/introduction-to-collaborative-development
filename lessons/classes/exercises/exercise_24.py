class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return float(self._x)

    @property
    def y(self):
        return float(self._y)

    @x.setter
    def x(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("the value must be a `float` type.")

        self._x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("the value must be a `float` type.")

        self._y = value

    def distance_to_origin(self):
        return (self.x*self.x+self.y*self.y)**(1/2)

    def __add__(self, point2):
        return Coordinate(self.x+point2.x, self.y+point2.y)

    def __sub__(self, point2):
        return Coordinate(self.x-point2.x, self.y-point2.y)
