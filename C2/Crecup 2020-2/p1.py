'''
Retorna una lista de tuplas, cada una de las cuales corresponde a una de las ciudades del pais indicado en el archivo.
(ciudad,año_menor_pob,menor_población,año_mayor_pob,mayor_población)
Como sugieren los nombres, cada tupla contiene el nombre de la ciudad, el año en que se contabilizó la
menor población para esa ciudad (string), la menor población (entero), el año con el mayor registro (string),
y la mayor población (entero). Puede suponer que nunca habrá empates.
'''
def min_max(nombre_arch, pais):
    arch = open(nombre_arch)
    ciudades = {} #nombre_ciudad : [año_menor, val_menor, año_may, val_may]
    for line in arch:
        line = line.strip().split(',')

        if pais == line[2]:
            anio, ciud, _, pob, _ = line
            pob = int(pob)

            if ciud not in ciudades:
                ciudades[ciud] = [0, 9999999, 0, -1]
            
            if pob > ciudades[ciud][3]:
                ciudades[ciud][2] = anio
                ciudades[ciud][3] = pob
            if pob < ciudades[ciud][1]:
                ciudades[ciud][0] = anio
                ciudades[ciud][1] = pob
    
    arch.close()
    res = []

    for city in ciudades:
        año_menor, val_menor, año_may, val_may = ciudades[city]
        res.append((city, año_menor, val_menor, año_may, val_may))
    
    return res

print(min_max('ciudades.txt','United States'))

