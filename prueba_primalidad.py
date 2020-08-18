def es_primo(valor):
    contador = 0
    for i in range(1, valor + 1):
        if i == 1 or i == valor:
            continue
        if valor % i == 0:
            contador = contador + 1
    if contador > 0:
        return False
    else:
        return True
    

def run():
    numero = int(input("ingresa un número "))
    if es_primo(numero) == True:
        print("es primo")
    else:
        print("no es primo")


if __name__ == "__main__":
    run()