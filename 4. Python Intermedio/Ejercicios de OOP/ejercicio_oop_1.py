import math
class Circle():
    def __init__(self, radius):
        print("A new circle has been created! ")
        self.radius = radius

    def get_area (self):
        area = math.pi* self.radius**2
        #print(f"The area of the circle is {area}!")
        return area
        

new_circle = Circle(5)
print(f"The area of the circle is {new_circle.get_area()}")
