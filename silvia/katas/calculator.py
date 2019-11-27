def calcula(numero):
    operador = input()
    segundo_numero = int(input())
    
    if operador == '+':
        segundo_numero = numero + segundo_numero
    elif operador == '-':
        segundo_numero = numero - segundo_numero
    elif operador == '*':
        segundo_numero = numero * segundo_numero
    elif operador == '/':
        segundo_numero = numero / segundo_numero
    print(segundo_numero)
    calcula(segundo_numero)

primer_numero = int(input())
calcula(primer_numero)

