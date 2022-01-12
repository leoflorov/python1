# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигур


import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        # Длина стороны по координатам точек
        def side_len(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        # Длина стороны ab
        self.ab = side_len(self.a, self.b)
        self.bc = side_len(self.b, self.c)
        self.ac = side_len(self.c, self.a)

    # Площадь треугольника
    def triangle_area(self):
        semi_perimeter = self.triangle_perimeter() / 2
        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.ab)
                         * (semi_perimeter - self.bc)
                         * (semi_perimeter - self.ac))

    # Периметр треугольника
    def triangle_perimeter(self):
        return self.ab + self.ac + self.bc

    # Высота треугольника
    def triangle_height(self):
        return self.triangle_area() / (self.ab / 2)


triangle_1 = Triangle((5, 4), (8, 9), (0, 12))

print(f"Площадь = {triangle_1.triangle_area()}")
print(f"Высота = {triangle_1.triangle_height()}")
print(f"Периметр = {triangle_1.triangle_perimeter()}")


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.


class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        # Функция вычисляет длину стороны согласно координатам точек
        def side_len(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        def triangle_area(len1, len2, len3):
            semi_perimeter = (len1 + len2 + len3) / 2

            return math.sqrt(semi_perimeter
                             * (semi_perimeter - len1)
                             * (semi_perimeter - len2)
                             * (semi_perimeter - len3))

        self.ab = side_len(self.a, self.b)
        self.bc = side_len(self.b, self.c)
        self.cd = side_len(self.c, self.d)
        self.da = side_len(self.d, self.a)
        self.diagonal_ac = side_len(self.c, self.a)
        self.diagonal_bd = side_len(self.b, self.d)
        self.perimeter = self.ab + self.bc + self.cd + self.da


        # представим трапецию как 2 треугольника и сложим 2 площади этих треугольников
        self.area = triangle_area(self.ab, self.diagonal_bd, self.da) \
                    + triangle_area(self.diagonal_bd, self.bc, self.cd)

    def is_equal_trapeze(self):
        if self.diagonal_ac == self.diagonal_bd:
            return True
        return False
