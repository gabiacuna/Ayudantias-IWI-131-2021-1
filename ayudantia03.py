if 5:
    print(True)


if not -1:
    print(False)

a = 3

# Importancia identacion
if a < 4:
    print('3 es menor a 4!')
elif a == 5:
    b = 6
print('a es igual a 5')

# If anidados:

if a > 0:
    if a > 8:
        print('a es mayor a 8')

if a > 0 and a < 8:
    print('a es mayor a 8')

b = 43
c= -23

if b >= c:
    print(b, "es mayor que", c)
elif b == 43:        
    print(b, "es igual a 43")   #Nunca va a correr, por que?
elif b < a:
    print(b, "es menor que", a)
else:
    print(b, "es menor que", c, "\n", b, "es distinto de 43\ny", a, "es mayor que", b)