
# a = ''

# print(bool(a))

# a = "Hola mundo!<3"
# b = 'Hooola'

# index = 0

# for i in a:
#     print('a['+str(index)+'] = ' + i)
#     index += 1

# index = -1

# while index != (-len(a) - 1):
#     print('a['+str(index)+'] = ' + a[index])
#     index -= 1

# c = 8
# d = 2

# print('1', a[c:d:-1])
# print('2', a[d:c])
# print('3', a[1::2])

# a = a[0:5] + 'kiwi' + a[10:len(a)]

# print(a.lower())


# def contar(letra, palabra):
#     res = 0
#     for i in palabra:
#         if letra == i:
#             res += 1
#     return res

# cuenta cuantas veces aparece letra en palabra
def contar(letra, palabra):  # letra, str de 1 caracter ; palabra, str 1 o + caracteres
    res = 0

    for i in palabra:   # i es un caracter de palabra
        if i == letra:
            res += 1

    return res

# [x] votos = int('ABCD') nota entre 1 y 7
# [x] return : Cancion mejor evaluada
# [x] if ninguna nota >= 4, return : ''
# [x] Empate da lo mismo cual retorna


def mejor(votos):

    max_votos = 0

    votos = str(votos)
    A = int(votos[0])  # Nota de A
    B = int(votos[1])
    C = int(votos[2])
    D = int(votos[3])

    if A < 4 and B < 4 and C < 4 and D < 4:  # Para no contar si todos son < a 4
        return ''

    for i in votos:  # Buscar el max
        if int(i) >= max_votos:
            max_votos = int(i)

    if A == max_votos:  # Retornar el Max
        return 'A'
    elif B == max_votos:
        return 'B'
    elif C == max_votos:
        return 'C'
    return 'D'


print(mejor(1223))

voto = int(input('Voto? '))

# Contadores cant de votos:
A = 0
B = 0
C = 0
D = 0

while voto != -1:

    bestCanc = mejor(voto)  # Uso func anterior

    if 'A' == bestCanc:
        A += 1
    elif 'B' == bestCanc:
        B += 1
    elif 'C' == bestCanc:
        C += 1
    elif 'D' == bestCanc:
        D += 1

    voto = int(input('Voto? '))

# print('A=', A)
# print('B=', B)
# print('C=', C)
# print('D=', D)

max_votos = 0
win = ''
win_v = 0
# Busqueda del max
if A > B and A > C and A > D:
    win = 'A'
    win_v = A
elif B > A and B > C and B > D:
    win = 'B'
    win_v = B
elif C > B and C > A and C > D:
    win = 'C'
    win_v = C
else:
    win = 'D'
    win_v = D

print('La favorita es', win, ' con ', win_v, ' votos.')
