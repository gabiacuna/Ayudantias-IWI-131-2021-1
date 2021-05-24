#Ciclos :D

#Determinada Cantidad de veces

cont = 0

while cont < 4:
    print(cont)

    cont += 1

# Mientras una condicion se cumple

a = ''
b = '00000'
print()

while a != b:
    a += '0'
    print(a)

print('b:',b)
print('a:',a)

#FLAGS!

#en if

if cont != 0:
    flag = False
else:
    flag = True

if not flag:
    print('Paso algo!')

cont = 0
flag = True

#en while

while flag:
    print('el while esta corriendo!')

    cont += 4

    if cont >= 10:
        flag = False


'''
Ejemplos:
'''


# pot = 0
# res = 0

# while pot < 10:
#     res += n**pot
#     pot += 1

# print(res)

# 5! = 1*2*3*4*5

#Factorial: 

# res = 1

# while n > 0:
#     res *= n
#     n -= 1

# print(res)

#Conteo:
# n = int(input('ingrese un numero:\t'))
# cont = 0

# while n > 0:
#     n -= 1

#     m = int(input('num:\t'))

#     if m % 3 == 0:
#         cont += 1

# print(cont, 'num eran multiplos de 3')


#max/min

n = int(input('ingrese un numero:\t'))

mayor = 9999

while n > 0:
    n -= 1
    m = int(input('num:\t'))

    if mayor > m:
        mayor = m

print('el mayor es:\t', mayor)
