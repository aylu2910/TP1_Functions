def cantDeBilletes(monto):
    Billetes500 = int(monto/500)
    Billetes100 = int((monto-(Billetes500*500))/100)
    Billetes50 = int((monto-(Billetes500*500+Billetes100*100))/50)
    Billetes10 = int((monto-(Billetes500*500+Billetes100*100+Billetes50*50))/10)
    Billetes5 = int((monto-(Billetes500*500+Billetes100*100+Billetes50*50+Billetes10*10))/5)
    Billetes1 = int(monto-(Billetes500*500+Billetes100*100+Billetes50*50+Billetes10*10+Billetes5*5))

    print ("Cantidad de dinero ingresado: ", monto)
    print ("Cantidad de dinero en Billetes de $500: ",Billetes500)
    print ("Cantidad de dinero en Billetes de $100: ",Billetes100)
    print ("Cantidad de dinero en Billetes de $50: ",Billetes50)
    print ("Cantidad de dinero en Billetes de $10: ",Billetes10)
    print ("Cantidad de dinero en Billetes de $5: ",Billetes5)
    print ("Cantidad de dinero en Billetes de $1: ",Billetes1)

total_compra = int(input("Ingrese el total de la compra: "))
dinero_recibido = int(input("Ingrese el dinero recibido: "))
if dinero_recibido < total_compra:
    print("El dinero recibido es insuficiente")
else:
    if total_compra == dinero_recibido:
        print("No hay vuelto")
    else:
        diferencia = dinero_recibido - total_compra
        cantDeBilletes(diferencia)

