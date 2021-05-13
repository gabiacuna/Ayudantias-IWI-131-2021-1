def es_palindromo(num):  # num es un int
    num = str(num)
    num_inv = num[::-1]

    if num == num_inv:
        return True
    return False


print(es_palindromo(12321))

num = input('Ingrese un num palindómico')
pasos = 0


while num != num[::-1]:
    pasos += 1
    suma = int(num) + int(num[::-1])
    num = str(suma)
    print('intermedio = ', num)
print(pasos)
print(num)
