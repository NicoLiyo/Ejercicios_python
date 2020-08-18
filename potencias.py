# def run():
#   ex = 1
#   ni = 1
#   limite = 1000
#   while ni <= limite:
#       print (ni)
#       ni = 2 ** ex
#       ex = ex +1 
    
# if __name__ == "__main__":
#   run()


# def run():
#   frase = input("ingrese una frase")
#   for i in frase:
#       if i == "s": 
#           continue
#       print(i)


def run():
    a = int(input("ingrese un número"))
    b = int(input("ingrese un número"))
    c = a + b
    contador = 0
    while contador < c:
        if c == 8:
            break
        print("no es 8")
        contador += 1

        
if __name__ == "__main__":
    run()