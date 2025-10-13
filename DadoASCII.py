import os
import time
import random

Titulo = ("\033[1;37m"+"                                                                                                          \n"                                         
                   "  ▒▒▒▒▒▒░    ▒▒▒▒▒▒░  ▒▒▒▒▒▒░      ▒▒▒▒░      ▒▒▒▒▒▒▒░    ▒▒▒▒▒▒▒░  ▒▒▒▒▒▒▒░  ▒▒░  ▒▒░                    \n"
                   "  ▒▒░   ▒▒░  ▒▒░ ▒▒░  ▒▒░   ▒▒░  ▒▒░   ▒▒░    ▒▒░  ▒▒░  ▒▒░         ▒▒░       ▒▒░  ▒▒░                    \n"
                   "  ▒▒░   ▒▒░  ▒▒░ ▒▒░  ▒▒░   ▒▒░  ▒▒░   ▒▒░    ▒▒░  ▒▒░    ▒▒▒▒▒░    ▒▒░       ▒▒░  ▒▒░                    \n"
                   "  ▒▒░   ▒▒░  ▒▒▒▒▒▒░  ▒▒░   ▒▒░  ▒▒░   ▒▒░    ▒▒▒▒▒▒▒░         ▒▒░  ▒▒░       ▒▒░  ▒▒░                    \n"
                   "  ▒▒▒▒▒▒░    ▒▒░ ▒▒░  ▒▒▒▒▒▒░      ▒▒▒▒░      ▒▒░  ▒▒░  ▒▒▒▒▒▒▒░    ▒▒▒▒▒▒▒░  ▒▒░  ▒▒░  (Por Javier MGB)  \n")
print(Titulo)

Barra = ("========================================================================================")
print(Barra)

estados_dado = {1: "  ____________    \n "
                   "|            |   \n "
                   "|            |   \n "
                   "|      ■     |   \n "
                   "|            |   \n "
                   "|____________|  ",
                2: "  ____________    \n "
                   "|            |   \n "
                   "|   ■        |   \n "
                   "|            |   \n "
                   "|        ■   |   \n "
                   "|____________|  ",
                3: "  ____________    \n "
                   "|            |   \n "
                   "|   ■        |   \n "
                   "|      ■     |   \n "
                   "|        ■   |   \n "
                   "|____________|  ",
                4: "  ____________    \n "
                   "|            |   \n "
                   "|   ■    ■   |   \n "
                   "|            |   \n "
                   "|   ■    ■   |   \n "
                   "|____________|  ",
                5: "  ____________    \n "
                   "|            |   \n "
                   "|   ■    ■   |   \n "
                   "|      ■     |   \n "
                   "|   ■    ■   |   \n "
                   "|____________|  ",
                6: "  ____________    \n "
                   "|            |   \n "
                   "|   ■    ■   |   \n "
                   "|   ■    ■   |   \n "
                   "|   ■    ■   |   \n "
                   "|____________|  ",
                }


def limpiar_consola():
    os.system("cls")        

def tirar_dado():
    input("Presiona Enter para tirar el dado...")
    print("Tirando el dado...")

    for x in range(20):
        print(Titulo)
        print(Barra)

        numero = random.randint(1, 6)
        print(estados_dado[numero])   

        time.sleep(0.5)  
        limpiar_consola() 

    return numero

def resultado(numero):
    print(Titulo)
    print(Barra)
    print("El número que ha salido es: ", numero)
    print(estados_dado[numero])
    

def principal():
    resultados = []
    while True:
        numero = tirar_dado()

        resultado(numero)
        resultados.append(numero)

        otra_vez = input("¿Quieres tirar el dado de nuevo? (s/n): ")

        if otra_vez != 's':
            break

    print("Gracias por jugar. ¡Hasta la próxima!")

principal()