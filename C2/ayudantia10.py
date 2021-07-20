
ojos = {'humanx': 2, 'araña': 8, 'mosca': 5, 'girafa': 2 }

#Si la llave no existe, se agrega
ojos['gato'] = 2
#Si la llave si existe, se modifica su valor
ojos['humanx'] = 3

#Usar del para borrar un elemento
del ojos['humanx']  #La llave DEBE existir en el dict, si no arroja error

#Cant de pares llave-valor
cantLlaves = len(ojos)

#comprobar si una llave esta eb el dict
check = 'araña' in ojos #-> se usa en los for!!!

for especie in ojos:
   print(especie, 'tiene', ojos[especie], 'ojos')


### Ejercicios:

#P2

# (cancion, album, artistas, f echa evaluacion, nota)
evaluaciones = [  
   ('Phypocrita', 'Hasta abajo', ['Pynuel'], (2018, 6, 30), 4),
   ('Sin Phyjama', 'Nuevo Estilo', ['Becky T', 'Turize'], (2018, 4, 14), 3),
   ('Vaina Crazy', 'del Weno', ['Ozune', 'Turize'], (2018, 7, 18), 5),
   ('Phypocrita', 'Hasta abajo', ['Pynuel'], (2018, 8, 20), 5),
   ('Quiero Beber Agua', 'Hasta abajo', ['Pynuel'], (2018, 2, 25), 5),
]

'''
Pregunta (a)
Retornar diccionario donde la llave es el nombre del artista y el valor es una
lista de enteros con las evaluaciones de canciones en las que ha participado.
'''

def notas_por_artista(lista):
   res = {} # artista : [notas]
   for cancion, album, artistas, fecha, nota in lista:
      for art in artistas:
         if art not in res:
            res[art] = []
         res[art].append(nota)
   return res

print(notas_por_artista(evaluaciones))
#{'Ozune': [5], 'Pynuel': [4, 5, 5], 'Becky T': [3], 'Turize': [3, 5]}

'''
Pregunta (b)
Retornar lista con los 3 artistas que con mayor probabilidad producen hits,
ordenada de forma descendente según la probabilidad.
La probabilidad se obtiene al dividir la cantidad de evaluaciones del artista
con nota 4 o 5 entre la cantidad total de evaluaciones del artista
En ambos considerar las evaluaciones hasta la fecha consultada, inclusive.
Si hay menos de 3 artistas con evaluaciones anteriores a la fecha,
entregue una lista con todos los artistas posibles.
Tenga en consideracion que los 3 mejores artistas seleccionados deben tener
probabilidad ≥ a todo el resto de los artistas en SpotiPhy.
'''

# (A,M,D) <= (A,M,D)

def artistas_hit(lista, fecha):
   notas = notas_por_artista(lista)
   probHit = {}   #artista:prob
   for cancion, album, artistas, fechaL, nota in lista:
      if fechaL <= fecha:
         for art in artistas:
            if art not in probHit:
               probHit[art] = 0
            if nota in [4, 5]:
               probHit[art] += 1
   
   top = [] #(prob, artista)

   for artista in probHit:
      probHit[artista] /= len(notas[artista])

      top.append((probHit[artista], artista))

   top.sort()
   top.reverse()

   res = []
   i = 0
   for prob, nombre in top:
      res.append(nombre)
      if i == 2:
         return res
      i+=1
   return res

print(artistas_hit(evaluaciones,(2018,8,30)))
#['Pynuel', 'Ozune', 'Turize']
print(artistas_hit(evaluaciones,(2018,2,28)))
# ['Pynuel']

#P3

repartidores = {
   'rayo macuin': ((10, 2), True), 'reparti dhor': ((9, 3), True),
   'eliseo al-azar': ((5, 5), False)}

usuarios = {1221: (5, 2), 441: (8, 2), 587: (10, 1)}

visitas = {
   'rayo macuin': [(1221, 5), (441, 8), (587, 2)],
   'reparti dhor': [(1221, 2), (441, 5), (587, 3)],
   'eliseo al-azar': [(1221, 8), (441, 2), (587, 1)],
}

'''
Retornar una lista de repartidores disponibles y cercanos, ordenados de manera
descendente, según el numero de visitas que hayan realizado al usuario.
Un repartidor será considerado cercano si está ubicado a menos de 4 km del
usuario. Si no hay repartidores cercanos, retornar una lista vacía.
'''

def buscar_repartidor(repartidores,usuarios,visitas,codigo):
   xU, yU = usuarios[codigo]

   res = [] #(nVisitas, repartidor)

   for nombreR in repartidores:
      if repartidores[nombreR][1]:
         xR, yR = repartidores[nombreR][0]

         dist = ((xR-xU)**2 + (yR-yU)**2)**(1/2)

         if dist <= 4:
            notVis = True
            for idCliente, nVisitias in visitas[nombreR]:
               if idCliente == codigo:
                  res.append((nVisitias, nombreR))
                  notVis = False
            if notVis:
               res.append((0, nombreR))
   
   res.sort()
   res.reverse()

   resTherial = []

   for visitas, nombre in res:
      resTherial.append(nombre)
   
   return resTherial

print(buscar_repartidor(repartidores,usuarios,visitas,587))
# ['reparti dhor', 'rayo macuin']
print( buscar_repartidor(repartidores,usuarios,visitas,441))
# ['rayo macuin', 'reparti dhor']
print( buscar_repartidor(repartidores,usuarios,visitas,1221))
# []
            
