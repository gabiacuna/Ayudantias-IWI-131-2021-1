# P2:
semana = 'lunes,martes,miercoles,jueves,viernes'


def altaCong(horario, dia):
    hora = int(horario[:2])
    mins = int(horario[3:])
    # hora = int(hora[:2]) + (int(hora[3:])/60) mejor solucion :)

    if dia in semana:

        cong = (7 == hora and 30 <= mins) or (
            9 == hora and 30 >= mins) or (7 < hora < 9)

        if cong == False:
            cong = (17 == hora and 30 <= mins) or (
                20 == hora and 0 == mins) or (17 < hora < 20)

    else:
        cong = (8 == hora and 30 <= mins) or (
            11 == hora and 0 == mins) or (8 < hora < 11)

        if cong == False:
            cong = (17 == hora and 45 <= mins) or (
                22 == hora and 30 >= mins) or (17 < hora < 22)

    return cong


def auto(dia, horario, cPasaj):
    cong = altaCong(horario, dia)

    if dia in semana:
        if cong:
            if cPasaj >= 3:
                return 0
            return 2400
        else:
            return 2000 - (100*cPasaj)

    if cong:
        return 4500 - (300*cPasaj)
    return 2800


def camion(dia, horario):
    cong = altaCong(horario, dia)

    if dia in semana:
        if cong:
            return 3500
        return 2500
    if cong:
        return 4500
    return 3800


tipoV = input('Tipo Vehiculo: ')
dia = input('Dia: ')
horario = input('Horario: ')

if tipoV == 'auto':
    cPasaj = int(input('Cantidad Pasajeros: '))
    precio = auto(dia, horario, cPasaj)
else:
    precio = camion(dia, horario)

print('Total a pagar: ', precio)
