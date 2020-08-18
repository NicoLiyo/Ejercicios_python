def cambio(divisa):
    dinero = int(input("Inidque el monto a cambiar $"))
    print("usted desea cambiar $" + str(dinero) + divisa + " a dolar")
    div = dinero / relacion
    camb = round (div, 2)
    print("el cambio es de $" + str(camb) + " dolares")


texto_inicial = """ Ingrese la opción de moneda que desea cambiar a dolar:

                    1) Peso Chileno
                    2) Peso Argentino
                    3) Peso Colombiano   """

e = 0
while e == 0:
    e = 1
    opcion = int(input(texto_inicial))

    if opcion == 1:
        relacion = 700
        cambio(" pesos chilenos")
    elif opcion == 2:
        relacion = 65
        cambio(" pesos argentinos")
    elif opcion == 3:
        relacion = 250
        cambio(" pesos colombianos")
    else:
        print("opción no válida")
        e = 0






