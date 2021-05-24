def mayor(l,c,m):
    pte1 = 'La mayor venta realizada fue de '
    pte2 = ' y la realizo '
    if l > c and l > m:
        return pte1 + str(l)+ pte2 + 'larry'
    elif c > l and c > m:
        return pte1 + str(c)+ pte2 + 'curly'
    return pte1 + str(m)+ pte2 + 'moe'

def menor(l,c,m):
    pte1 = 'El vendedor que menos a vendido es '
    if l < c and l < m:
        return pte1 + 'larry'
    elif c < l and c < m:
        return pte1 + 'curly'
    return pte1 + 'moe'


menu = '''
1.- Ingresar ventas
2.- Venta mayor
3.- Peor vendedor
0.- Salir
'''
print(menu)

oper = input('Operacion?')

vLarry = 0
vCurly = 0
vMoe = 0

while oper != '0':
    if oper == '1':
        vend = input('Nombre vendedor: ')
        cantV = int(input('Cantidad vendida: '))
        if vend == 'larry':
            vLarry += cantV
        elif vend == 'curly':
            vCurly += cantV
        elif vend == 'moe':
            vMoe += cantV
    
    elif oper == '2':
        print(mayor(vLarry, vCurly, vMoe))
    
    elif oper == '3':
        print(menor(vLarry, vCurly, vMoe))
    
    else:
        print('Operacion no existe')
    
    oper = input('Operacion?')
    
print('moe vendio:', vMoe, 'productos')
print('larry vendio:', vLarry, 'productos')
print('curly vendio:', vCurly, 'productos')
