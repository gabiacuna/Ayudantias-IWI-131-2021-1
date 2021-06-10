def kokoro(disp):
    disp[0][1] ='▄'
    disp[0][3] = '▄'
    disp[1][0] = '▄'
    disp[1][2] = '▄'
    disp[1][4] = '▄'
    disp[2][0] = '▄'
    disp[2][-1] = '▄'
    disp[3][1] = '▄'
    disp[3][3] = '▄'
    disp[4][2] = '▄'

    return disp

def ajedrez(disp):
    for i in range(len(disp)):
        for j in range(len(disp[i])):
            if i%2 == 0 and j%2 == 0:
                disp[i][j] = '▄'
            elif i%2 != 0 and j%2 != 0:
                disp[i][j] = '▄'
    return disp

def cuad(disp):
    for i in range(len(disp[0])):
        disp[0][i] = '▄' 
        disp[-1][i] = '▄' 
        disp[i][0] = '▄' 
        disp[i][-1] = '▄' 
    return disp

def cross(disp):
    for i in range(len(disp)):
        for j in range(len(disp[i])):
            if i == (len(disp[i])-1-j):
                disp[i][j] = '▄'
            elif i == j:
                disp[i][j] = '▄'

    return disp

disp = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
]

fill = '▄'

temp =cross(disp)

for i in temp:
    print(i)
