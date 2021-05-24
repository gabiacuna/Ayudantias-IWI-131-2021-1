#Ayu Listas I

lista1 = []
lista2 = list()
lista3 = ['hola',7,(3+2),4,True,2,('h'=='H'.lower()),8.2,5]
lista4 = list('hola mundito!')

print(lista1)
print(lista2)
print(lista3)
print(lista4)

rango = range(0,10,2)    #range(inicio, fin, salto) 
print('\n', rango, ':\t', list(rango))

print('\n~~~~\n')

for i in range(len(lista3)):
    print('lista3[' + str(i) + '] :', lista3[i])


print('\nLista3 antes:\t', lista3)

lista3[-1] = 'Esto cambio'

print('\nLista3 despues:\t', lista3)
