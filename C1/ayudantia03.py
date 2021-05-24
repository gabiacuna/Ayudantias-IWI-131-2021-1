'''
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

if 0 < a < 8:
    print("a es mayor a 8")

a = 3
b = 43
c= 55

if b >= c:
    print(b, "es mayor que", c)
elif b == 43:        
    print(b, "es igual a 43")   #Nunca va a correr, por que?
elif b < a:
    print(b, "es menor que", a)
else:
    print(b, "es menor que", c, "\n", b, "es distinto de 43\ny", a, "es mayor que", b)

h = 'Hola'

#Ej 1:

clase = input('Clase del demonio:')

if clase == 'especial':
    print('Un misil podria funcionar.')
elif int(clase) == 1:
    print("Incluso un tanque podria no ser suficiente.")



#EJ 2:

n_clases_i = int(input('Numero de clases impartidas:\n'))
n_clases_a = int(input('Nuemro de clases asistidas:\n'))
just = input('Esta justificadx?\n')



poc = (n_clases_a*100)/n_clases_i

poc = round(poc)

print('Asistencia:', poc, '%')

if just == 'Si':
    print('Puedes dar el examen :)')
elif 80 > poc >= 75 :
    print('Puedes dar el examen justito :D')
elif poc >= 75:
    print('Puedes dar el examen')
else:
    print('No lo puedes dar')

'''


agno = int(input())
a = agno % 19
print(a)
b = agno % 4
print(b)
c = agno % 7
print(c)
d = (19 * a + 24)%30
print(d)
e = (2 * b + 4 * c + 6 * d +5)%7
print(e)
n = 22 + d + e
print(n)

if n<=31:
    mes = 3

else:
    n= n-31
    mes = 4
print(n,"/",mes,"/",agno)