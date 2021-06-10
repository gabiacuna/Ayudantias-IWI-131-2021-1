#Ayu Listas I

from random import choice

lista1 = []
lista2 = list()
lista3 = ['hola',7,(3+2),4,True,2,('h'=='H'.lower()),8.2,5]
lista4 = list('hola mundito!')

print(lista1)
print(lista2)
print(lista3)
print(lista4)

rango = range(0,3,1)    #range(inicio, fin, salto) 
print('\n', rango, ':\t', list(rango))

print('\n~~~~\n')

for i in range(len(lista3)):
    print('lista3[' + str(i) + '] :', lista3[i])


print('\nLista3 antes:\t', lista3)

lista3[-1] = 'Esto cambio'

print('\nLista3 despues:\t', lista3)


#Metodos:
lista_test = list(range(5))
x = [-23,56]
lista_test.append(x)
print(lista_test)
lista_test.count(x)
print(lista_test)
lista_test.index(x)
print(lista_test)
lista_test.remove(x)
print(lista_test)
lista_test.reverse()
print(lista_test)
lista_test.sort()
print(lista_test)
lista_test.insert(3,x)
print(lista_test)

print('~~~~~~')

lista_uno = [1,2,3]
lista_dos = list(lista_uno)
del lista_dos[1]
print(lista_uno)
print(lista_dos)

a = choice(lista3)
b = choice(lista3)
c = choice(lista3)

print('~~~~~~')

print('a:\t', a)
print('b:\t', b)
print('c:\t', c)