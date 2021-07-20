file = open('deniro.csv')
file_new = open('analisis_deniro.txt', 'w')

top = []    #[(puntaje, nombre pelicula)]
decadas = {}

for line in file:
    if 'Title' not in line:
        line = line.strip()
        line = line.split(', ')
        
        anio, p, nombre = line
        top.append((p, nombre, anio))
        dec = anio[2]

        if dec not in decadas:
            decadas[dec] = 0
        decadas[dec] += 1

        
    
top.sort()

file_new.write('\t- 5 Peliculas con mayor Puntuacion en RT:\n')

for ptos, nombre, _ in top[-1:-6:-1]:
    file_new.write(nombre + ' ' + ptos + '\t' + '\n')

file_new.write('\n\n\t- Cantidad de peliculas en las que participo por decada:\n')

for dec in decadas:
    file_new.write(dec + '0\'\t' + str(decadas[dec]) + '\n')

prim5 = []

for ptos, nombre, a in top:
    prim5.append((a,nombre))

prim5.sort()
file_new.write('\n\n\t- Primeras 5 pelis:\n')

for a, nombre in prim5[0:5]:
    file_new.write(nombre + '\n')

file_new.write('\n\n\t- Ultimas 5 pelis:\n')

for a, nombre in prim5[-5:]:
    file_new.write(nombre + '\n')  

file.close()
file_new.close()