from os import system
from time import sleep
from colorama import init, Fore, Style
import util
if system("cls") !=0: system("clear")
init(autoreset=True)

# Retos opcionales
# Editar o eliminar vuelos
# Guardar / cargar aeropurtos y vuelos 'JSON'
# Mostrar estadisticas (vuelo mas largo, promedio de km)
# Colores en la 'CLI' usadno el modulo colorama 




while True:
    print(Fore.BLUE + "_____________________   _______________   __________________")
    print(Fore.BLUE + "||1-Añadir aeropuerto || 2-Añadir vuelo || 3-Listar vuelos||")
    print(Fore.BLUE + "---------------------   ---------------   ------------------")
    print(Fore.BLUE + "_________________________________  __________")
    print(Fore.BLUE + "||4-Buscar vuelos por aeropuerto || 5-Salir||")
    print(Fore.BLUE + "---------------------------------  ----------")
    op = int(input(Fore.WHITE + "Opción: "))
    if op == 1: # 1 opción
        util.nuevo_aeropuerto(util.aeropuertos)

    elif op == 2: # 2 opción
        util.nuevo_vuelo(util.vuelos, util.aeropuertos)

    elif op == 3: # 3 opción
        print("\n")
        print("Vuelos")
        print("------")
        util.listar_vuelos(util.vuelos)
        sleep(2)
        print("\n")

    elif op == 4: # 3 opción
        util.buscar_por_aeropuerto(util.vuelos)

    elif op == 5: #5 opción
        util.clear_terminal() #Limpia la terminal
        print("Cerrando gestor.")
        sleep(0.5)
        util.clear_terminal()
        print("Cerrando gestor..")
        sleep(0.5)
        util.clear_terminal()
        print("Cerrando gestor...")
        sleep(0.5)
        util.clear_terminal()
        break

