import random


def menu() -> int:
    print ("Menu")
    print ("[1] Jugar \n[2] Salir")
    option: int = -1
    try:
        option = int(input("Ingrese el número de opción: "))
    except ValueError: 
        print ("Ingrese un valor NUMERICO")
    return option


def main():
    option: int = -1
    while option != 2:
        option = menu()
        if option == 1:
            print("iniciando el juego...")
        elif option == 2:
            print("Saliendo...")
        else:
            print("Ingrese una opción valida")


main()