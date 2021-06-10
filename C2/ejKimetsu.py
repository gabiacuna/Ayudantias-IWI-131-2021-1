'''
+---+-------------------+------+--------+-------+---------------------------------------------+
|   | nombre apellido   | edad | altura | raza  | amigxs                                      |
+---+-------------------+------+--------+-------+---------------------------------------------+
| 0 | Inosuke Hashibira | 15   | 1.64   | Human | 'Tanjiro' , 'Zenitsu'                       |
+---+-------------------+------+--------+-------+---------------------------------------------+
| 1 | Tanjiro Kamado    | 13   | 1.65   | Human | 'Kanao','Nezuko','Inosuke','Giyu','Kyojuro' |
+---+-------------------+------+--------+-------+---------------------------------------------+
| 2 | Nezuko Kamado     | 12   | 1.53   | Demon | 'Tanjiro','Inosuke','Mitsuri'               |
+---+-------------------+------+--------+-------+---------------------------------------------+
| 3 | Mitsuri Kanaroji  | 19   | 1.67   | Human | 'Nezuko','Kyojuro'                          |
+---+-------------------+------+--------+-------+---------------------------------------------+
'''

kimetsu = [
    ['Inosuke Hashibira',15,1.64,'Human',['Tanjiro','Zenitsu','Shinobu','Kanao','Kotoha','Aoi']],
    ['Tanjiro Kamado',13,1.65,'Human',['Kanao','Nezuko','Inosuke','Giyu','Shinobu','Zeintsu','Urokodaki']],
    ['Nezuko Kamado',12,1.53,'Demon',['Tanjiro','Inosuke','Mitsuri']],
    ['Zenitsu Agatsuma',16,1.645, 'Human',['Tanjiro','Nezuko','Kaigaku','Jigoro','Inosuke','Shinobu']],
    ['Mitsuri Kanaroji',19,1.67,'Human',['Nezuko','Kyojuro']],
    ['Shinobu Kocho', 18, 1.51, 'Human', ['Giyu', 'Tanjiro', 'Zeintsu','Inosuke','Murata','Kanao','Tomayo']]
]

def amig_en_comun(kimetsu, per1, per2): #Solo tenemos nombre, no apellido
    res = []

    for x in range(len(kimetsu)):
        nombre_apellido = kimetsu[x][0]
        n2 = nombre_apellido.split(' ')
        if n2[0] == per1:
            ami1 = list(kimetsu[x][4])
        elif n2[0] == per2:
            ami2 = list(kimetsu[x][4])
    
    for amigx in ami1:
        if amigx in ami2:
            res.append(amigx)
    return res

def orden_esp(kimetsu,index):
    for i in range(len(kimetsu)):
        temp = kimetsu[i][index]
        kimetsu[i].insert(0,temp)
    kimetsu.sort()
    for i in range(len(kimetsu)):
        del kimetsu[i][0]
    return kimetsu




# print(amig_en_comun(kimetsu,'Inosuke' ,'Tanjiro'))
# prueba =['ab','aab','cd','bc']
# prueba.sort()
# print(prueba)
x = orden_esp(kimetsu, 0)

for i in x:
    print(i)
