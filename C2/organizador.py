


def desplegar_tablero(tablero, estados):    #tablero['listados_tareas'][estado] = [{tarea, fecha_limite},....]
    #print('\ntab\n',tablero)
    print('+++ TABLERO', tablero['nombre'].upper() ,'+++\n')
    for estado in estados:
        print('TAREAS', estado.upper())
        index = 0
        for tarea in tablero['listados_tareas'][estado]:
            print(str(index) + '.',tarea['descripcion'], '; Límite:', tarea['fecha_limite'])
            index += 1

        print('---')






def crear_tablero(nombre, estados):
    tab = {'nombre':nombre}

    tareas = {}
    for estado in estados:
        tareas[estado] = []
    
    tab['listados_tareas'] = tareas

    return tab

def crear_tarea(descripcion, fecha_limite):
    return {'descripcion' : descripcion, 'fecha_limite' : fecha_limite}

def agregar_tarea(tablero, tarea):

    if 'Por hacer' in tablero['listados_tareas']:
        tablero['listados_tareas']['Por hacer'].append(tarea)
        return tablero
    if 'Sin Estado' not in tablero['listados_tareas']:
        tablero['listados_tareas']['Sin Estado'] = []
    tablero['listados_tareas']['Sin Estado'].append(tarea)
    return tablero

def mover_tarea(tablero):
    lista1 = input('Ingrese el nombre de la lista de origen: ')
    pos1 = input('Ingrese la posision en la lista de origen: ')
    
    lista2 = input('Ingrese el nombre de la lista objetivo: ')
    pos2 = input('Ingrese la posision en la lista objetivo: ')

    tarea = tablero['listados_tareas'][lista1][int(pos1)]

    del tablero['listados_tareas'][lista1][int(pos1)]

    tablero['listados_tareas'][lista2].append(tarea)

    return tablero



estados = ['Por hacer', 'En Progreso', 'En espera', 'Terminadas']

tablero = crear_tablero('Personal', estados)

print(tablero)

task = crear_tarea('Pasear al perro', (2021, 7, 3))

tablero = agregar_tarea(tablero, task)

print(tablero)

tablero = mover_tarea(tablero)

desplegar_tablero(tablero, estados)
'''
>>> crear_tablero('Personal', ['Por hacer', 'En Progreso', 'En espera', 'Terminadas'])
tablero = {'nombre' : 'Personal', 'listados_tareas' = {'Por hacer' : [], 'En Progreso' : [], 'En espera' : [], 'Terminadas' : []}}

>>> crear_tarea('Pasear al perro', (2021, 7, 3))
{'descripcion' : 'Pasear al perro', 'fecha_limite' : (2021, 7, 3)}

>>> agregar_tarea(tablero, {'descripcion' : 'Pasear al perro',
'fecha_limite' : (2021, 7, 3)})
tablero = {'nombre' : 'Personal', 'listados_tareas' = {'Por hacer' :
[{'descripcion' : 'Pasear al perro', 'fecha_limite' : (2021, 7, 3)}], 'En
Progreso' : [], 'En espera' : [], 'Terminadas' : []}
'''
