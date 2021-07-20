'''
El valor de marca es un indicador monetario que mide la fuerza de una marca en el mercado, a partir
de los activos financieros que la rodean. Tenemos un archivo que registra el valor de marca de muchas
empresas a nivel mundial, en distintas fechas. Las lı́neas de este archivo tienen el siguiente formato:

año-mes-dı́a,marca,paı́s,valor,rubro

Observe que los elementos que componen cada fecha están separados por guiones. Además de la marca y
su valor, cada lı́nea registra también el paı́s de origen de la marca y el rubro al que pertenece, que es un
texto en Inglés.
'''

'''
La función debe considerar únicamente marcas del rubro y año que fueron
indicados en los parámetros, y debe crear un archivo para cada paı́s que contenga marcas que cumplen
el filtro.

Los archivos deben contener las marcas ordenadas de mayor a menor valor, considerando cada
marca una única vez con su mayor valor en el año considerado.

debe retornar el número total de paı́ses distintos que se
consideraron, es decir, la cantidad de archivos que fueron creados.
'''
def f(nombre_arch, rubro, año):
    arch = open(nombre_arch)

    paises = {} #{pais : {marca : mayor valor}}

    for line in arch:
        line = line.strip().split(',')
        
        a,_,_ = line[0].split('-')

        if a == año and line[-1] == rubro:
            _, marca,pais,valor,_ = line

            valor = int(valor)

            if pais not in paises:
                paises[pais] = {}
            
            if marca not in paises[pais]:
                paises[pais][marca] = 0

            if valor > paises[pais][marca]:
                paises[pais][marca] = valor
            
    arch.close()

    f_line = 'Mayor valor en ' + año +' de las marcas del rubro ' + rubro + ':\n'

    for pais in paises:
        txt = []
        for marca in paises[pais]:
            txt.append((paises[pais][marca], marca))
        txt.sort()
        txt.reverse()

        n_arch = open(pais + '.txt', 'w')

        n_arch.write(f_line)

        for val, marca in txt:
            line = '\tMarca: ' + marca +', valor en US$: ' + str(val) + '000\n'
            n_arch.write(line)
        n_arch.close()
    
    return len(paises)

print(f('marcas.txt','Fast-Moving Consumer Goods','2016'))
