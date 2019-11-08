import math

def hypotenuse():
    leg_one = int(input('Dime cuanto mide el primer cateto: '))
    leg_two = int(input('Dime cuanto mide el segundo cateto: '))

    hypotenuse = round(math.sqrt(pow(leg_one, 2) + pow(leg_two, 2)), 2)
    return hypotenuse

print(f'La hipotenusa es {hypotenuse()}')