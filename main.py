import random

def menu_principal() -> None:
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Jugar")
        print("2. Salir")
        opcion: str = input("Elige una opción: ")
        if opcion == "1":
            jugar()
        elif opcion == "2":
            print("¡Gracias por jugar, hasta pronto!")
            return
        else:
            print("Opción no válida.")


def crear_mazo()-> list[str]:
    return ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


def jugar()->None:
    palo: str = random.choice(["Corazones", "Diamantes", "Picas", "Tréboles"])
    mazo: list[str] = crear_mazo()
    monedas: int = 15
    camino: list[str] = crear_camino(15)
    posicion: int = 0
 
    print(f"\nTu mazo es del palo de {palo} y empiezas con {monedas}")
 
    while True:
        mostrar_camino(camino, posicion)
        input("Presiona Enter para avanzar una etapa...")
        posicion = posicion + 1
 
        match camino[posicion]:
            case "Enemigo":
                monedas = combate(mazo, monedas)
                if monedas == 0:
                    print("¡Has perdido la partida!")
                    return
            case "Moneda":
                ganadas: int = random.randint(3, 7)
                monedas = monedas + ganadas
                print(f"¡Encontraste {ganadas} monedas! Ahora tienes{monedas}")
            case "Carta":
                carta: str = random.choice(["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])
                mazo.append(carta)
                print("¡Encontraste la carta", carta + "! Tu mazo ya tiene", len(mazo), "cartas.")
            case "Victoria":
                print("\n¡¡¡VICTORIA!!! Llegaste al final del camino.")
                return
            case _:
                print("Etapa vacía, no pasa nada.")


def crear_camino(total_etapas:int)-> list[str]:
    enemigos: int = total_etapas // 2 -1
    monedas: int = random.randint(0,2)
    cartas: int = random.randint(0,3)
    vacios = total_etapas - monedas - cartas - (enemigos-1) - 3

    eventos: list[str] = ["Enemigos"* 5]
    eventos = ["Moneda"]* monedas
    eventos = ["cartas"]* cartas
    eventos = ["Vacio"]* vacios
    random.shuffle(eventos)
    return ["Vacio"]+eventos+["Enemigo","Victoria"]


def combate(mazo_jugador: list[str] , monedas_jugador: int)-> int
    mazo_enemigo = crear_mazo()
    monedas_enemigo = 10
    ganancias = 0

    while monedas_jugador>0 and monedas_enemigo>0:
        cartas_jugador = random.sample(mazo_jugador,2)
        cartas_enemigo = random.sample(mazo_enemigo, 2)
        apuesta_jugador = random.randint(1,min(5,monedas_jugador))
        apuesta_enemigo = random.randint(1,min(5,monedas_enemigo))
        puntos_jugador = valores_cartas(cartas_jugador)
        puntos_enemigo = valores_cartas(cartas_enemigo)



        if puntos_jugador>21:
            print("¡Perdiste!")

        if puntos_jugador == puntos_enemigo and puntos_enemigo != 21:
            print("Empate , nadie pierde monedas.")
            print(f"Tus puntos fueron {puntos_jugador} y los de tu enemigo fueron {puntos_enemigo}")
            print(f"Tus cartas jugadas fueron {cartas_jugador}")
            
        elif puntos_jugador>puntos_enemigo:
            monedas_enemigo -= apuesta_enemigo
            ganancias = monedas_enemigo + apuesta_enemigo
            print(f"Ganaste")
            print(f"Tus puntos fueron {puntos_jugador} y los de tu enemigo fueron {puntos_enemigo}")
            print(f"Tus cartas jugadas fueron {cartas_jugador}")

        else:
            print("Pierdes la ronda")
            print(f"Tus puntos fueron {puntos_jugador} y los de tu enemigo fueron {puntos_enemigo}")
            print(f"Tus cartas jugadas fueron {cartas_jugador}")
            monedas_jugador -= apuesta_jugador
            
        print(f"Monedas jugador: {monedas_jugador} | Monedas enemigo: {monedas_enemigo}")
        monedas_jugador += ganancias
    


def valores_cartas(cartas: list[str]) -> int:
    suma_valores = 0
    for carta in cartas:
        if carta == "A":
            suma_valores += 11
        elif carta in ["J","Q","K"]:
            suma_valores +=10
        else:
            suma_valores += int(carta)    
        if suma_valores > 21:
            suma_valores -= 10
    return suma_valores
    