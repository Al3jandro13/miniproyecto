# Mini Proyecto 1 - Fundamentos de Algoritmos y Programación
# Integrantes:
# Juan David Quintero
# Alejandro Luna
# Juan Sebastian Lopez
#
# Uso de IA generativa: (explicar aquí cómo, por qué y para qué se usó la IA.
# Ejemplo: "Usamos Claude para revisar y corregir errores de nuestro código;
# luego lo revisamos y lo entendimos para la sustentación.")

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


def crear_mazo() -> list[str]:
    return ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


def jugar() -> None:
    palo: str = random.choice(["Corazones", "Diamantes", "Picas", "Tréboles"])
    mazo: list[str] = crear_mazo()
    monedas_jugador: int = 15
    camino: list[str] = crear_camino(15)
    posicion: int = 0

    print(f"\nTu mazo es del palo de {palo} y empiezas con {monedas_jugador} monedas.")

    while True:
        mostrar_camino(camino, posicion)
        input("Presiona Enter para avanzar una etapa...")
        posicion = posicion + 1

        match camino[posicion]:
            case "Enemigo":
                monedas_jugador = combate(mazo, monedas_jugador)
                if monedas_jugador == 0:
                    print("¡Has perdido la partida!")
                    return
            case "Moneda":
                ganadas: int = random.randint(3, 7)
                monedas_jugador = monedas_jugador + ganadas
                print(f"¡Encontraste {ganadas} monedas! Ahora tienes {monedas_jugador}")
            case "Carta":
                carta: str = random.choice(crear_mazo())
                mazo.append(carta)
                print(f"¡Encontraste la carta {carta}! Tu mazo ya tiene {len(mazo)} cartas.")
            case "Victoria":
                print("\n¡¡¡VICTORIA!!! Llegaste al final del camino.")
                return
            case _:
                print("Etapa vacía, no pasa nada.")


def crear_camino(total_etapas: int) -> list[str]:
    enemigos: int = total_etapas // 2 - 1
    monedas: int = random.randint(0, 2)
    cartas: int = random.randint(0, 3)
    # Etapas del medio: se descuentan la primera, la penúltima (Enemigo) y la última (Victoria)
    vacios: int = total_etapas - monedas - cartas - (enemigos - 1) - 3

    eventos: list[str] = ["Enemigo"] * (enemigos - 1)
    eventos = eventos + ["Moneda"] * monedas
    eventos = eventos + ["Carta"] * cartas
    eventos = eventos + ["Vacío"] * vacios
    random.shuffle(eventos)
    return ["Vacío"] + eventos + ["Enemigo", "Victoria"]


def mostrar_camino(camino: list[str], posicion: int) -> None:
    line: str = ""

    for i in range(len(camino)):
        if i == posicion:
            line = line + "[J]"
        elif i == 0:
            line = line + "[I]"
        elif i <= posicion + 2:  # se desvelan 2 etapas por delante
            line = line + ("[ ]" if camino[i] == "Vacío" else "[" + camino[i][0] + "]")
        else:
            line = line + "[?]"
    print("\n" + line)
    print("J=Tú  I=Inicio  E=Enemigo  M=Moneda  C=Carta  V=Victoria  ?=Oculta")


def combate(mazo_jugador: list[str], monedas_jugador: int) -> int:
    mazo_enemigo: list[str] = crear_mazo()
    monedas_enemigo: int = 10
    ganancias: int = 0  # monedas ganadas, se suman al final de la partida

    print(f"\n¡Un enemigo te reta! Tú tienes {monedas_jugador} monedas y él {monedas_enemigo}")

    while monedas_jugador > 0 and monedas_enemigo > 0:
        cartas_jugador: list[str] = random.sample(mazo_jugador, 2)
        cartas_enemigo: list[str] = random.sample(mazo_enemigo, 2)
        apuesta_jugador: int = random.randint(1, min(5, monedas_jugador))
        apuesta_enemigo: int = random.randint(1, min(5, monedas_enemigo))
        puntos_jugador: int = valores_cartas(cartas_jugador)
        puntos_enemigo: int = valores_cartas(cartas_enemigo)

        print(f"\nTus cartas: {cartas_jugador} = {puntos_jugador} | apuestas {apuesta_jugador}")
        print(f"Cartas enemigo: {cartas_enemigo} = {puntos_enemigo} | apuesta {apuesta_enemigo}")

        if puntos_jugador > 21:  
            puntos_jugador = 0
        if puntos_enemigo > 21:
            puntos_enemigo = 0

        if puntos_jugador == puntos_enemigo and puntos_enemigo != 21:
            print("Empate, nadie pierde monedas.")
        elif puntos_jugador > puntos_enemigo:
            print("¡Ganas la ronda!")
            monedas_enemigo -= apuesta_enemigo
            ganancias += apuesta_enemigo
        else:  
            print("Pierdes la ronda.")
            monedas_jugador -= apuesta_jugador

        print(f"Monedas jugador: {monedas_jugador} | Monedas enemigo: {monedas_enemigo}")

    if monedas_jugador > 0:
        print(f"\n¡Derrotaste a tu enemigo! Cobras {ganancias} monedas.")
        return monedas_jugador + ganancias
    print("\nTe quedaste sin monedas...")
    return 0


def valores_cartas(cartas: list[str]) -> int:
    suma_valores: int = 0
    for carta in cartas:
        if carta == "A":
            suma_valores += 11
        elif carta in ["10", "J", "Q", "K"]:
            suma_valores += 10
        else:
            suma_valores += int(carta)
    if suma_valores > 21:  
        suma_valores -= 10
    return suma_valores


menu_principal()