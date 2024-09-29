import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print(f"Point: ({self.x}, {self.y})")

class Ellipse(Point):
    def __init__(self, x, y, a, b):
        super().__init__(x, y) 
        self.a = a  
        self.b = b  

    def area(self):
        return math.pi * self.a * self.b

class Circle(Ellipse):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, radius)  

    def area(self):
        return math.pi * self.a ** 2  


if __name__ == "__main__":
   
    x = float(input("Nhập tọa độ x của tâm elip: "))
    y = float(input("Nhập tọa độ y của tâm elip: "))
    a = float(input("Nhập bán trục lớn (a) của elip: "))
    b = float(input("Nhập bán trục nhỏ (b) của elip: "))
    
    ellipse = Ellipse(x, y, a, b)
    print(f"Diện tích elip: {ellipse.area()}")

    
    radius = float(input("Nhập bán kính của đường tròn: "))
    
    circle = Circle(x, y, radius)
    print(f"Diện tích đường tròn: {circle.area()}")
