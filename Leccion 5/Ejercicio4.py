import math
while True:
    velocidad = float (input ("Introduce la velocidad del viento: "))
    temperatura = float (input ("Introduce la temperatura en grados Farenheite: "))
    if (0 <= velocidad <= 4):
        sencacionTermica = temperatura
        print("Índice de sensación térmica: ",sensacionTermica)
        print("-----------------------------")
    elif (velocidad >= 45):
        sensacionTermica = 1.6 * temperatura - 55
        print("Índice de sensación térmica: ",sencacionTermica)
        print("-----------------------------")
    else:
        sencacionTermica = 91.4 + (91.4 - temperatura)*(0.0203 * (math.sqrt (velocidad) - 0.474))
        print("Índice de sensación térmica: ",sencacionTermica)
        print("-----------------------------")
