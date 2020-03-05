while (True):
	tornillo=int(input("Escriba la cantidad de pernos que desea llevar:"))
	tuercas=int(input("Escriba la cantidad de tuercas que desea llevar:"))
	arandelas=int(input("Escriba la cantidad de arandelas que desea llevar:"))
	if(tornillo!=tuercas):
		print("Compruebe la orden")
		print("-----------------------------")
	else:
		operacion=((tornillo*5)+(tuercas*3)+(arandelas*1))
		print("La orden esta bien, costo total: "+str(operacion))
		print("-----------------------------")
