from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    def calculate_area(self):
        self.area = math.pi * self.radius **2
        return self.area
        
    def calculate_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        return self.perimeter
    
    def __str__(self):
        return f"Circle of radius {self.radius}"

class Square(Shape):
    def __init__(self,side):
        super().__init__()
        self.side = side
    def calculate_area(self):
        self.area = self.side ** 2
        return self.area
        
    def calculate_perimeter(self):
        self.perimeter = self.side * 4
        return self.perimeter
    
    def __str__(self):
        return f"Square of side {self.side}"

class Triangle(Shape):
    def __init__(self,side_a,side_b,side_c):
        super().__init__()
        if (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a):
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
        else:
            raise ValueError(f"The sides {side_a}, {side_b}, and {side_c} cannot create a triangle.")

    def calculate_area(self):
        self.semi_perimeter = (self.side_a + self.side_b + self.side_c)/2
        self.area = math.sqrt(self.semi_perimeter *(self.semi_perimeter-self.side_a)*(self.semi_perimeter-self.side_b)*(self.semi_perimeter-self.side_c))
        return self.area

    def calculate_perimeter(self):
        self.perimeter = self.side_a + self.side_b + self.side_c
        return self.perimeter
    
    def __str__(self):
        return f"Triangle of sides: {self.side_a},{self.side_b} and {self.side_c}"


shape_square = Square(5)
shape_circle = Circle(4)
shape_triangle = Triangle(2,5,4)
shapes = [shape_square,shape_circle,shape_triangle]


for s in shapes:
    # :.2f  ->  ":" separate the variable from the rules, ".2" means the precision of the number and "f" treats the number as float
    print(f"The area of {s} is {s.calculate_area():.2f} ")
    print(f"The perimeter of {s} is {s.calculate_perimeter():.2f}")