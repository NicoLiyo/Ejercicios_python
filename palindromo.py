def palindromo(palabra):
    palabra_aux = palabra.replace(" ", "")
    palabra_aux = palabra_aux.lower()
    palabra_inv = palabra_aux[::-1]
    if palabra_inv == palabra_aux:
        return True
    else:
        return False

def salir():
    opcion = input("salir S/N?")
    if opcion == "S":
        return False
    else:
        return True


def run():
    palabra = input("ingresa una palabra o frase (EXIT para salir) ")
    palabra_evaluar = palindromo(palabra)
    if palabra_evaluar == True:
        print("es palindromo")
    else:
        print("no es palindromo")
    return palabra


if __name__ == "__main__":
    encendido = True
    while encendido == True:
        run()
        encendido = salir()
    
    