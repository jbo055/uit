
class Rectangle2D:
    def __init__(self, x = 0, y = 0, width = 0, height = 0):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width cannot be negative")
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height cannot be negative")
        self._height = value

    def getArea(self):
        return self._width * self._height
    
    def getPerimeter(self):
        return 2 * (self._width + self._height)
    
    def containsPoint(self, x, y):
         return (self._x - self._width / 2 <= x <= self._x + self._width / 2) and \
               (self._y - self._height / 2 <= y <= self._y + self._height / 2)
    
    def contains(self, rectangle):
        return (self.containsPoint(rectangle.x - rectangle.width / 2, rectangle.y - rectangle.height / 2) and
                self.containsPoint(rectangle.x + rectangle.width / 2, rectangle.y + rectangle.height / 2))
    
    def overlaps(self, rectangle):
        return not (self._x + self._width / 2 <= rectangle._x - rectangle._width / 2 or
                    self._x - self._width / 2 >= rectangle._x + rectangle._width / 2 or
                    self._y + self._height / 2 <= rectangle._y - rectangle._height / 2 or
                    self._y - self._height / 2 >= rectangle._y + rectangle._height / 2)

    def __lt__(self, other):
        return self.getArea() <other.getArea()
    
    def __le__(self, other):
        return self.getArea() <= other.getArea()

    def __eq__(self, other):
        return self.getArea() == other.getArea()

    def __ne__(self, other):
        return self.getArea() != other.getArea()

    def __gt__(self, other):
        return self.getArea() > other.getArea()

    def __ge__(self, other):
        return self.getArea() >= other.getArea()
    
    def __contains__(self, other):
        return self.contains(other)
    
    def __str__(self):
        return f"Rectangle2D({self._x}, {self._y}, {self._width}, {self._height})"

# Test kode   
def main():
    r1 = Rectangle2D(0, 0, 10, 5)
    r2 = Rectangle2D(1, 1, 5, 3)
    print(f"r1.getArea(): {r1.getArea()}")
    print(f"r1.getPerimeter(): {r1.getPerimeter()}")
    print(f"r1.containsPoint(3, 3): {r1.containsPoint(3, 3)}")
    print(f"r1.contains(r2): {r1.contains(r2)}")
    print(f"r1.overlaps(r2): {r1.overlaps(r2)}")
    print(f"r1 < r2: {r1 < r2}")
    print(f"r1 <= r2: {r1 <= r2}")
    print(f"r1 == r2: {r1 == r2}")
    print(f"r1 != r2: {r1 != r2}")
    print(f"r1 > r2: {r1 > r2}")
    print(f"r1 >= r2: {r1 >= r2}")
    print(f"r2 in r1: {r2 in r1}")
    print(f"r1: {r1}")
    print(f"r2: {r2}")

if __name__ == "__main__":
    main()

