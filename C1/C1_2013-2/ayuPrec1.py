# Calcular Tarifa
#                   L-V (H. cong)  L-V finde(H.C)  finde
# Autos + pasajeros
# Camiones

# hora formato HH:MM

semana = 'lunes martes miercoles jueves viernes'


def hConges(hora_og, dia):  # True si es hora de cong, False si no
    hora = int(hora_og[:2])
    minu = int(hora_og[3:])

    # hora = int(hora[:2]) + (int(hora[3:])/60)

    res = False

    if dia in semana:
        if (hora == 7 and minu >= 30) or (hora == 9 and minu <= 30) or hora == 8:
            res = True
        elif (hora == 17 and minu >= 30) or (hora == 20 and minu == 00) or 17 < hora < 20:
            res = True
    else:
        if (hora == 8 and minu >= 30) or (hora == 11 and minu == 00) or 8 < hora < 11:
            res = True
        elif (hora == 17 and minu >= 45) or (hora == 22 and minu <= 30) or 17 < hora < 22:
            res = True

    return res


def auto(horario, dia, pasaj):  # retorna tarifa
    cong = hConges(horario, dia)

    if (dia in semana) and (cong):
        if pasaj >= 3:
            return 0
        return 2400
    elif (dia in semana) and (not cong):
        return 2000 - (100 * pasaj)

    if cong:
        return 4500 - (300 * pasaj)
    return 2800


def camiones(horario, dia):

    cong = hConges(horario, dia)

    if (dia in semana) and (cong):
        return 3500
    elif (dia in semana) and (not cong):
        return 2500

    if cong:
        return 4500
    return 3800


tipoV = input('Tipo Vehiculo: ')
dia = input('Dia: ')
horario = input('Horario: ')

if tipoV == 'auto':
    pasaj = int(input('Pasajeros: '))
    precio = auto(horario, dia, pasaj)
else:
    precio = camiones(horario, dia)

print('Total a pagar: ', precio)
