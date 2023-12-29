from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def area(self, radius):
        print('Area of circle is:', 3.1416 * radius**2)


class Rectangle(Shape):
    def area(self, length, bredth):
        print('Area of rectangle is:', length * bredth)


circle = Circle()
circle.area(5)