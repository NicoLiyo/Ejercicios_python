import random

def contrasena():
    lista_mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lista_min = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lista_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    lista_simb = ["@", "#", "$", "%", "&"]
    caracteres = lista_mayus + lista_min + lista_num + lista_simb
    clave = []
    for i in range(15):
        caracter = random.choice(caracteres)
        clave.append(caracter)
    clave = "".join(clave)
    return clave

def run():
    contrasenas = contrasena()
    print("tu contraseña es: " + contrasenas)


if __name__ == "__main__":
    run()
