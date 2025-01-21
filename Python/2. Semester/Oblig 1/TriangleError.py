# 13.12 ( The TriangleError class) Define an exception class named TriangleError that 
# extends RuntimeError. The TriangleError class contains the private data fields 
# side1, side2, and side3 with accessor methods for the three sides of a triangle. 
# Modify the Triangle class in Programming Excercise 12.1 to throw a TriangleError 
# exception if the three given sides cannot form a triangle.

# Triangle class
class Triangle:
    def __init__(self, side1, side2, side3)