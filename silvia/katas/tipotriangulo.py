# Crear una clase tiángulo que rebiba un imput con los tres lados
# Al instanciar, hacer un print que diga qué tipo de triángulo es:
# equilátero, isósceles o rectángulo

import math


class Triangle():
    def __init__(self, side_one, side_two, side_three):
        self.side_one = side_one
        self.side_two = side_two
        self.side_three = side_three

    @property
    def type_of_triangle(self):
        sides_list = [self.side_one, self.side_two, self.side_three]
        sides_list_oredered = sorted(sides_list)
        if pow(sides_list_oredered[2], 2) == pow(sides_list_oredered[1], 2) + pow(sides_list_oredered[0], 2):
            return 'rectángulo'
        if self.side_one == self.side_two == self.side_three:
            return 'equilátero'
        if (self.side_one == self.side_two) and (self.side_two != self.side_three):
            return 'isósceles'
        else:
            return 'escaleno'

    def __repr__(self):
        return f'El primer lado mide {self.side_one}\nEL segundo lado mide {self.side_two}\nEl tercer lado mide {self.side_three}\nEl triángulo es de tipo {self.type_of_triangle}'


first_side = float(input('Dame la medida del primer lado: '))
second_side = float(input('Dame la medida del siguiente lado: '))
third_side = float(input('Dame la medida del último lado: '))

example_triangle = Triangle(first_side, second_side, third_side)
print(example_triangle)
