
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def scale(self, factor):
        self.width *= factor
        self.height *= factor

    def describe(self):
        if self.is_square():
            return f"Square {self.width} x {self.height}"
        return f"Rectangle {self.width} x {self.height}"


r = Rectangle(4, 3)
s = Rectangle(5, 5)

print(r.area(), r.perimeter())
print(r.is_square(), s.is_square())

r.scale(2)

print(r.width, r.height, r.area())
print(s.area())
