import random

# Se define el menu inicial
# para que el jugador 
# visualice las opciones

def menu() -> int:
    print ("Menu")
    print ("[1] Jugar \n[2] Salir")
    option: int = -1
    try:
        option = int(input("Ingrese el número de opción: "))
    except ValueError: 
        print ("Ingrese un valor NUMERICO")
    return option


def cartas():
    # Definimos en 2 listas los palos 
    # pertenecientes a la baraja inglesa
    # y los valores que tienen las cartas
    
    valores: list[str] = ["2", "3", "4", "5", "6", "7", "8", "9", " 10", "J", "Q", "K", "A"]
    palos: list[str] = ["Diamantes", "Picas", "Treboles", "Corazones"]
    
    # Mediante random tomamos 2
    # cartas y un palo al azar
    
    valor_1 = random.choice(valores)
    valor_2 = random.choice(valores)
    palo_elegido = random.choice(palos)
    
    # Mientras los valores de las 
    # cartas sean iguales , reasignamos
    # el valor de valor_2
    # mediante random 

    
    while valor_1 == valor_2:
        valor_2 = random.choice(valores)
        
    # Definimos los valores 
    # internos si las letras son J, Q, K o A
        
    valor_interno_1 = valor_1
    valor_interno_2 = valor_2

    # Funcion para definir el valor
    # de las cartas J, Q, K y A
    # si el valor es A, entonces
    # puede tener un valor de 1 o 11
    
    def convertir(valor:str) -> int | list[int]:
        if valor in ["J","Q","K"]:
            return 10
        if valor == "A":
            return [1, 11]   
        return int(valor)
   
    return convertir(valor_interno_1), convertir(valor_interno_2), palo_elegido, valor_1, valor_2

def main():
    option: int = -1
    while option != 2:
        option = menu()
        if option == 1:
            print("iniciando el juego...")
            mano = cartas()
            print(f"Cartas: {mano[2]}")
            
            
        elif option == 2:
            print("Saliendo...")
        else:
            print("Ingrese una opción valida")


main()