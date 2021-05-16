def vMayor(l, c, m):
    res1 = 'La mayor venta realizada fue de '
    res2 = ' y la realizo '

    if l > c and l > m:
        return res1 + str(l) + res2 + 'larry'
    elif c > l and c > m:
        return res1 + str(c) + res2 + 'curly'

    return res1 + str(m) + res2 + 'moe'


def vMenor(l, c, m):
    res1 = 'El vendedor que menos ha vendido es '

    if l < c and l < m:
        return res1 + 'larry'
    elif c < l and c < m:
        return res1 + 'curly'

    return res1 + 'moe'


menu = '1.- Ingresar ventas\n2.- Venta mayor\n3.- Peor vendedor\n0.- Salir'

print(menu)

vL = 0
vC = 0
vM = 0


opc = int(input('operacion? '))

while opc != 0:
    if opc == 1:
        vend = input('Vendenor? ')
        cant = int(input('cantidad? '))
        if vend == 'larry':
            vL += cant
        elif vend == 'curly':
            vC += cant
        else:  # asumimos inputs validos
            vM += cant
    elif opc == 2:
        print(vMayor(vL, vC, vM))
    elif opc == 3:
        print(vMenor(vL, vC, vM))
    else:
        print('La operacion no existe')

    opc = int(input('operacion? '))

print('moe vendio: ', vM)
print('larry vendio: ', vL)
print('curlu vendio: ', vC)
