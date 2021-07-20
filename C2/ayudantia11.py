siglas_enfermedades = {
	'LMA': 'Leucemia Mieloide Aguda'
	, 'IAM': 'Infarto Agudo al Miocardio'
    , 'C19': 'Coronavirus'
    , 'HCA': 'Hepatitis Cronica Activa', 'FQ': 'Fibrosis Quistica', 'ECV': 'Enfermedad Cerebro Vascular'
    , 'DBT': 'Diabetes', 'IRA': 'Insuficiencia Renal Aguda', 'TBC': 'Tuberculosis', 'TQC': 'Taquicardia'
    , 'UG': 'Ulcera Gastrica', 'EM': 'Esclerosis Multiple', 'M': 'Meningitis', 'OMA': 'Otitis Media Aguda'
    , 'PNF': 'Pielonefritis', 'EA': 'Alzheimer', 'NIH': 'Neumonia Intra-Hospitalaria'
    , 'IHO': 'Infeccion Herida Operatoria', 'HPT': 'Hipertension Pulmonar', 'EP': 'Embolismo Pulmonar'
    , 'CBP': 'Cirrosis Biliar Primaria', 'ARJ': 'Artritis Reumatoidea Juvenil', 'SLT': 'Sindrome de Lisis Tumoral'
    , 'VZV': 'Virus Varicela Zoster', 'TVP': 'Trombosis Venosa Profunda', 'EI': 'Endocarditis Infecciosa'
    , 'AE': 'Arterioesclerosis', 'HEL': 'Hemorragia Exterior Leve', 'RF': 'Resfriado Comun'
    , 'E1': 'Esquince Nivel 1', 'D': 'Depresion', 'ART': 'Artrosis', 'MG': 'Migrania', 'HL': 'Herpes Labial'
    , 'LG': 'Laringitis', 'FG': 'Faringitis', 'GMN': 'Glomerulonefritis'}

categorias_triage = {
    'C1': ['GMN', 'IAM', 'PNF', 'TVP', 'ECV', 'EP','C19'],
    'C2': ['LMA', 'TBC', 'NIH', 'IHO', 'HPT', 'FQ', 'SLT', 'IRA', 'M'],
    'C3': ['HCA', 'UG', 'EM', 'TQC'],
    'C4': ['DBT', 'CBP', 'VZV', 'ART', 'OMA'],
    'C5': ['EA', 'ARJ', 'HEL', 'RF', 'E1', 'D', 'MG', 'HL', 'LG', 'FG', 'EI']
}


# desde esta linea desarrolle su tarea

def ingresar_atenciones_por_sigla(lista_siglas, siglas_enfermedades, categorias_triage):
    diccionario = {"C1": 0, "C2": 0, "C3": 0, "C4": 0, "C5": 0}
    for sigla in lista_siglas:
        for llave, valores in categorias_triage.items():
            if sigla in valores:
                diccionario[llave] += 1
    return diccionario

def atencion_por_tiempo_de_espera(nombres_enfermedades,siglas_enfermedades, categorias_triage):
    lista = []
    res = []
    triag_orden = ["C1", "C2", "C3", "C4", "C5"]
    
    for enfermedad in nombres_enfermedades:
        for sigla in siglas_enfermedades:
            if siglas_enfermedades[sigla] == enfermedad:
                lista.append((sigla,enfermedad))
    print('Lista line 43:', lista)

    for cat in triag_orden:
        for categoria in categorias_triage:
            if cat == categoria:
                for siglaT in categorias_triage[categoria]:
                    for enfermedadL in lista:
                        if enfermedadL[0] == siglaT:
                            res.append(enfermedadL[1]) 
    return res

# Ejercicio 1
lista_siglas = ['ARJ', 'OMA', 'GMN', 'NIH', 'HCA', 'C19']
print (ingresar_atenciones_por_sigla(lista_siglas, siglas_enfermedades, categorias_triage))

# Ejercicio 2
nombres_enfermedades = ['Depresion', 'Meningitis', 'Infarto Agudo al Miocardio', 'Tuberculosis', 'Migrania',
                        'Otitis Media Aguda','Coronavirus']
print (atencion_por_tiempo_de_espera(nombres_enfermedades,siglas_enfermedades, categorias_triage))