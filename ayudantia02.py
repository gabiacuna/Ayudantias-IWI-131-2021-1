# Tip buena práctica: El importe de las librerias son lo primero que se debe escribir en su doc.
import math
from random import randint

# Funciones incluidas python

absTest = abs(32-940)
print("abs(32-940).....", absTest)

roundTest1 = round(0.26)
roundTest2 = round(0.26, 1)
print("round(0.26).....", roundTest1)
print("round(0.26, 1).....", roundTest2)

typeTest = type(absTest)
print("type(roundTest1).....", typeTest)

# Funciones incluidas de librerias

mathTest = math.exp(3)
print("math.exp(3).....", mathTest)

randTest = randint(0, 5)
print("randint(0, 5).....", randTest)

# Precedencia

precTest = (5 + 2 * 3) // 3

# Asosiatividad

asocTest = 3 // 7 % 3
