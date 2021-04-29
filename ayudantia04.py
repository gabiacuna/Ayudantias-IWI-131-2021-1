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

