from random import randint


# def unaFunc(a, b):  # a es in int (edad), b cantidad x (int)
#     res = (a + b)**2
#     a += 10

#     if a > 5:
#         return 'a es mayor que 5'

#     return 'a es menor o igual a 5'


# a = 9 ** (1/4)
# varX = unaFunc(5, 6)

# print(unaFunc(-5, 5) == unaFunc(5, -5))

'''
a = -5
b = 5
a = -5 + 10
a = 5
->  'a es menor o igual a 5'
a = 5
b = -5

a = 5 +10
a = 15

-> 'a es mayor que 5'

->'a es menor o igual a 5' == 'a es mayor que 5'
'''


# def cantAcido(cGel, cAgu):

#     if cGel > (cAgu/2):
#         res = cAgu + cAgu/2
#         return res
#     res = cGel + cGel*2
#     return res


# print(cantAcido(7, 9))


# 2 turnos
# funcion que nos diga si le achunto
# generar los numeros random

def jugada(intento, real):
    if intento == real:
        return 'le achunto'
    elif intento > real:
        return 'el num a adiv es menor'
    return 'el num a adiv es mayor'


n1 = input('Nombre jug 1: ')
n2 = input('Nombre jug 2: ')

intentos1 = 0
intentos2 = 0

randNum1 = randint(1, 5)
randNum2 = randint(1, 5)

turno = 1
hayGanador = '-'

while hayGanador == '-':
    if turno == 1:
        numTemp = int(input('Jug 1 ingresa tu intento'))

        res = jugada(numTemp, randNum1)
        if res == 'le achunto':
            hayGanador = '1'
        else:
            print(res)

        intentos1 += 1
        turno = 2
    elif turno == 2:
        numTemp = int(input('Jug 2 ingresa tu intento'))

        res = jugada(numTemp, randNum2)
        if res == 'le achunto':
            hayGanador = '2'
        else:
            print(res)
        intentos2 += 1
        turno = 1

if hayGanador == '1':
    print('Felicitaciones,', n1, ' ganaste! con', intentos1)
else:
    print('Felicitaciones,', n2, ' ganaste! con', intentos2)
