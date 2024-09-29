import math

class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def perimeter(self):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def area(self):
        raise NotImplementedError("This method should be overridden in subclasses.")


class Parallelogram(Polygon):
    def __init__(self, base, height):
        super().__init__(4)
        self.base = base
        self.height = height

    def perimeter(self):
        return 2 * (self.base + self.height)

    def area(self):
        return self.base * self.height


class Rectangle(Parallelogram):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.width = width

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length

    def area(self):
        return self.side_length ** 2

if __name__ == "__main__":
    square = Square(4)
    print("Hình vuông:")
    print("Chu vi:", square.perimeter())
    print("Diện tích:", square.area())

    rectangle = Rectangle(5, 3)
    print("\nHình chữ nhật:")
    print("Chu vi:", rectangle.perimeter())
    print("Diện tích:", rectangle.area())

    parallelogram = Parallelogram(6, 4)
    print("\nHình bình hành:")
    print("Chu vi:", parallelogram.perimeter())
    print("Diện tích:", parallelogram.area())
