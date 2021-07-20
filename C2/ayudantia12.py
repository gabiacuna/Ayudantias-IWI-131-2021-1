#Archivos de Txt :3

'''
aeiouAEIOU
0123456789

shrek -> $H5eK
'''

vocales = list('aeiouAEIOU')
print(vocales)


f = open('shrekscript.txt')
file_ok = open('shrekscript_noenc.txt', 'w')

appFiona = 0

for line in f:
    
    line = line.strip()
    line_buena = line.replace('$H5eK', 'shrek')
    
    for i in range(len(vocales)):
        if str(i) in line_buena:
            line_buena = line_buena.replace(str(i), vocales[i])
    if 'Fiona' in line_buena:
        appFiona += line_buena.count('Fiona')
    line_buena += '\n'
    file_ok.write(line_buena)

f.close()
file_ok.close()

print('Se menciona a Fiona', appFiona, 'veces.')