# Tipos de Datos
intEx = int()
intEx = 4324

floatEx = float()
floatEx = 3.14

booleEx = bool()
booleEx = True

strEx = str()
strEx = 'Miau'
strEx = "Guau"

# Tipos de Operadores

a = 5 + 6
b = 2 - 7
c = 654 / 342
d = 100 // 78
e = 3534 % 234
f = 2**5


#print (-a, -b)


# Precedencia

precTest = (5 + 2 * 3) // 3

# Asosiatividad

asocTest = 3 // 7 % 3

# Conversion de datos

castTest = 555

print(type(castTest))

castTest = str(castTest)

print(type(castTest))

# Entrada de datos:

inputTest = input("Ingresa un str")

# cualquier cosa que no sea vacio será true
inputTest2 = bool(input("Ahora ingresa un bool"))
print(inputTest2)