while True:
    PaqueteLibraA = float (input ("Precio por libra paquete A: "))
    PorcentajeMagroA = float (input ("Porcentaje magro del paquete A: "))
    PaqueteLibraB = float (input ("Precio por libra paquete B: "))
    PorcentajeMagroB = float (input ("Porcentaje magro del paquete B: "))
    CalcularA = PaqueteLibraA/PorcentajeMagroA
    CalcularB = PaqueteLibraB/PorcentajeMagroB
    print("Costo de carne Paquete A: ",CalcularA)
    print("Costo de carne Paquete B: ",CalcularB)
    if CalcularA > CalcularB:
        print("El paquete B es el mejor")
        print("-----------------------------")
    else:
        print("El paquete A es el mejor")
        print("-----------------------------")
