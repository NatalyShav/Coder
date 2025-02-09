def calc(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)


def circle_area(radius):
    """Вычисляет площадь круга по радиусу."""
    return math.pi * radius ** 2

def trapezoid_area(base1, base2, height):
    """Вычисляет площадь трапеции по основаниям и высоте."""
    return (base1 + base2) * height / 2

def square_area(side):
    """Вычисляет площадь квадрата по длине стороны."""
    return side ** 2

def rectangle_area(length, width):
    """Вычисляет площадь прямоугольника по длине и ширине."""
    return length * width

