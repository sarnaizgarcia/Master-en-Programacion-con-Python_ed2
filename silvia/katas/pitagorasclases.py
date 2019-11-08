import math

class RightTriangle():
    def __init__(self, leg_one, leg_two):
        self.leg_one = int(input('Dime cuanto mide el primer cateto: '))
        self.leg_two = int(input('Dime cuanto mide el segundo cateto: '))

    @property    
    def hypotenuse(self):
        h = round(math.sqrt(pow(self.leg_one, 2) + pow(self.leg_two, 2)), 0)
        return h
    
    def __repr__(self):        
        return f'El primer cateto es {self.leg_one}, el otro cateto es {self.leg_two} y la hipotenusa es {self.hypotenuse}'


triangle = RightTriangle(12, 9)
print(triangle) 