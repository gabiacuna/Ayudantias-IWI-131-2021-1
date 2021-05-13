
precioColOm = 5000
precioColPir = 6000
precioColSer = 20000
precioColBS = 5500

cantColOm = 3 * 20
cantColPir = 1 * 20
cantColSer = 2 * 20
cantColBS = 5 * 20

impuestoInOm = 3500
impuestoInPir = 0
impuestoInSer = 0
impuestoInBS = 22600

impuestoOm = 1.05
impuestoPir = 1
impuestoSer = 1.1
impuestoBS = 1.2

resOm = (precioColOm*cantColOm)*impuestoOm + impuestoInOm
resPir = (precioColPir*cantColPir)*impuestoPir + impuestoInPir
resSer = (precioColSer*cantColSer)*impuestoSer + impuestoInSer
resBS = (precioColBS*cantColBS)*impuestoBS + impuestoInBS


print(type(resOm), '\n')

print(int(resOm))

resOm = int(resOm)

print('\n', type(resOm))

print(resOm)
print(resPir)
print(resSer)
print(resBS)

print(resOm+resPir+resSer+resBS)
