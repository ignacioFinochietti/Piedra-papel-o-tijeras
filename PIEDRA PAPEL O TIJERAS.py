from random import randint
import random
jugador=0
opciones=["piedra", "papel", "tijeras"]
ganadas=0
perdidas=0
empates=0

print("Hola!, Bienvenido a piedra, papel o tijera")

while jugador != "cerrar":
    jugador=input("Para jugar debes elegir alguno o escribe cerrar para finalizar el programa: ")
    jugador=jugador.lower()
    

    if jugador == "cerrar":
        print("gracias por jugar!")
        quit()
    
    elif jugador != "piedra" and jugador != "papel" and jugador != "tijera":
        print("Error, Debe elegir entre las palabras piedra, papel o tijera")
    
    else:
        
        maquina= opciones[random.randint(0,2)]
        print("---------------------------")
        print ("Usted eligio", jugador)
        print("---------------------------")
        print("La maquina eligio", maquina)
        print("---------------------------")

        if jugador == maquina:
            print("Empate \U0001f937\u200D\u2642")
            empates = empates + 1

        elif jugador == "papel" and maquina == "piedra":
            print("Felicitaciones!, usted ganó \U0001f451")
            ganadas = ganadas + 1

        elif jugador == "papel" and maquina == "tijeras":
            print("Hoy no tuviste suerte, perdiste \u2639")
            perdidas = perdidas +1

        elif jugador == "piedra" and maquina == "tijeras":
            print ("Felicitaciones!, usted ganó \U0001f451")
            ganadas = ganadas + 1

        elif jugador == "piedra" and maquina == "papel":
            print("Hoy no tuviste suerte, perdiste \u2639")
            perdidas = perdidas +1

        elif jugador == "tijeras" and maquina == "papel":
            print ("Felicitaciones!, usted ganó \U0001f451")
            ganadas = ganadas + 1

        elif jugador == "tijeras" and maquina == "piedra":
            print ("Hoy no tuviste suerte, perdiste \u2639")
            perdidas = perdidas +1

        print("Ganaste: ", ganadas, "veces")
        print("Perdiste: ", perdidas, "veces")
        print("Empataste: ", empates, "veces")
        print("----------------------------------------")
