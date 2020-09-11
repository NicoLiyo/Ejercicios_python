def run():
    objetivo = int(input("ingresa un numero para calcular raiz cuadrada: "))
    opcion = int(input(""" 
    ingresa una opcion:  
    1:valor exacto 
    2:valor aproximado 
    3:valor aprox alternativo: 
    """))
    if opcion == 1:
        calcular1(objetivo)
    elif opcion == 2:
        calcular2(objetivo)
    elif opcion == 3:
        calcular3(objetivo)
    else:
        print("error")


def calcular1(valor):
    v_max = valor
    for v_min in range(v_max):
        test = v_min * v_min
        if test < valor:
            continue
        elif test == valor:
            print("la raiz cudrada de " + str(valor) + " es " + str(v_min))
            break
        else:
            print("El numero no tiene raiz cuadrada exacta")
            break


def calcular2(valor):
    epsilon = 0.01
    paso = 0.1 * epsilon
    test = 0
    while valor - test ** 2 > epsilon:
        test = test + paso
    print("la raiz cudrada de " + str(valor) + " es " + str(test))


def calcular3(valor):
    epsilon = 0.01
    v_max = max(1.0, valor)
    v_min = 0.0
    seccion = (v_max + v_min)/2
    while abs(valor - seccion**2) > epsilon:
        if seccion**2 < valor:
            v_min = seccion
        else:
            v_max = seccion
        seccion = (v_max + v_min)/2
        print("minimo " + str(v_min) + " maximo " + str(v_max))
    print("la raiz cudrada de " + str(valor) + " es " + str(seccion))


if __name__ == "__main__":
    run()