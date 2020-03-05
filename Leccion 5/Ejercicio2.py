while True:
	capTanque=float(input("ingrese la capacidad del tanque del combustible: "))
	indicadorGas=int(input("ingrese el porcentaje de gasolina de su vehiculo(100,75,50 o 25): "))
	millasGalon=float(input("¿Cuantas millas por galon gasta su vehiculo?: "))
	operacion=float((capTanque*(indicadorGas/100)*millasGalon))
	if(operacion>=200):
		print("Avanzara: "+" "+str(operacion)+" "+"millas con su combustible,es seguro continuar")
		print("-----------------------------")
	else:
		print("Avanzara: "+" "+str(operacion)+" "+"millas con su combustible,consigue gasolina")
		print("-----------------------------")
