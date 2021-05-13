
a = ''
print(bool(a))

a = "Hola mundo"
b = 'Hooola'

index = 0
for i in a:
    print('a['+str(index)+'] = ' + i)
    index += 1

index = -1

while index != (-len(a) - 1):
    print('a['+str(index)+'] = ' + a[index])
    index -= 1

c = 8
d = 2

print('1',a[c:d:-1])
print('2',a[d:c])
print('3',a[::2])


# def contar(letra, palabra):
#     res = 0
#     for i in palabra:
#         if letra == i:
#             res += 1
#     return res

