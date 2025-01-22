# 13.12 ( The TriangleError class) Define an exception class named TriangleError 
# that extends RuntimeError. The TriangleError class contains the private data 
# fields side1, side2, and side3 with accessor methods for the three sides of a 
# triangle. Modify the Triangle class in Programming Excercise 12.1 to throw a 
# TriangleError exception if the three given sides cannot form a triangle.

class TriangleError(RuntimeError):
    def __init__(self, side1, side2, side3):
        super().__init__("Invalid triangle sides.")
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    @property
    def side1(self):
        return self._side1
    
    @property
    def side2(self):
        return self._side2
    
    @property
    def side3(self):
        return self._side3

def is_valid(s1, s2, s3):
    return s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1    

class Triangle:
    def __init__(self, side1, side2, side3):
        if not is_valid(side1, side2, side3):
            raise TriangleError(side1, side2, side3)
        
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
    
    @property
    def side1(self):
        return self._side1
    
    @property   
    def side2(self):
        return self._side2
    
    @property
    def side3(self):
        return self._side3
    
    def perimeter(self):
        return self._side1 + self._side2 + self._side3

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self._side1) * (s - self._side2) * (s - self._side3)) ** 0.5

    def __str__(self):
        return f"Triangle with sides {self._side1}, {self._side2}, {self._side3} is a valid triangle. Perimeter: {self.perimeter()}, Area: {self.area()}"

try:
    test = Triangle(5, 5, 8)
    print(test)
except TriangleError as e:
    print(e)
