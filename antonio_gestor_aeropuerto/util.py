import os
import json
from colorama import init, Fore, Style
from time import sleep

init(autoreset=True)

aeropuertos =[] 

vuelos = [
    {"origen":"Madrid","destino": "Barcelona","id": "IB101", "km": 504, "plazas": 180}, #Madrid => Barcelona -- 1
    {"origen": "Barcelona","destino": "Malaga", "id": "VY450", "km": 770, "plazas": 160}, #Barcelona => Malaga -- 2
    {"origen": "Malaga","destino": "Madrid", "id": "UX333", "km": 430, "plazas": 220} #Malaga => Madrid -- 3

]




                                                               # Retos opcionales
# Editar o eliminar vuelos -- Terminado
# Guardar / cargar aeropurtos y vuelos 'JSON' -- Terminado
# Mostrar estadisticas (vuelo mas largo, promedio de km)
# Colores en la 'CLI' usadno el modulo colorama -- Terminado


#Funciones obligatorias

# Terminado
def clear_terminal():
    if os.name == "nt":  
        os.system("cls")
    else:  
        os.system("clear")

# Terminado
def introduce_codigo(msg):
    while True:
        codigo = input(msg)
        existe = False
        for aeropuerto in aeropuertos:
            if aeropuerto['codigo'] == codigo:
                existe = True
                break

        if len(codigo) == 3 and codigo.isalpha() and codigo.isupper() and not existe:
            print(Fore.GREEN + f"El codigo IATA '{codigo}' ha sido añadido")
            return codigo
        elif any(a['codigo'] == codigo for a in aeropuertos):
            print(Fore.RED + "Error: El codigo ya esta en la lista de aerpuertos")
        elif any(a['codigo'] == codigo for a in vuelos):
            print(Fore.RED + "Error: El codigo ya esta en la lista de vuelos")
        elif not codigo.isupper():
            print(Fore.RED + "Error: El codigo debe de estar en mayusculas")
        else:
            print(Fore.RED + "Error: El codigo debe contener solo letras")
 
# Terminada
def nuevo_aeropuerto(lista): #lista = aeropuertos
    codigo = introduce_codigo(Style.RESET_ALL + "Código IATA: ") #Funcion anterior (introduce_codigo())

    duplicado = False
    for i in lista: #lista = aeropuertos
        if i["codigo"] == codigo:
            duplicado = True
            break  
    if duplicado:
        print(Fore.RED + f"Error: Ya existe un aeropuerto con el código '{codigo}'.")
        return

    nombre = input("Introduce el nombre del aeropuerto: ").strip()
    ciudad = input("Introduce la ciudad: ").strip()

    nuevo = {
        "codigo": codigo,
        "nombre": nombre,
        "ciudad": ciudad
    }

    lista.append(nuevo)
    print(Fore.GREEN + f" Aeropuerto '{nombre}' añadido correctamente.")

#Terminado
def nuevo_vuelo(vuelos, aeropuertos):
    vuelo = input(Fore.WHITE + "¿Donde estas y donde quieres ir?(Origen => Destino): ").split(',')
    try:
        origen, destino = vuelo
    except ValueError:
        print(Fore.RED + "Error: Escribe 2 codigos IATA separados por una coma")
        return
    
    codigos = []
    for n in aeropuertos:
        codigos.append(n["codigo"])

    for vuelo in vuelos:
        if vuelo['origen'] == origen and vuelo['destino'] == destino:
            print(Fore.RED + "Error: Este vuelo ya existe")
            return

    vuelos.append({"origen": origen, "destino": destino,})
    print(Fore.GREEN + f"Vuelo añadido: {origen} → {destino}")


# Terminado    
def listar_vuelos(vuelos):
    
    for i, vuelo in enumerate(vuelos, start=1):
        print(Fore.YELLOW + f"{i}. {vuelo['origen']} => {vuelo['destino']} -- KM: {vuelo['km']}")

# Terminado
def buscar_por_aeropuerto(vuelos):
    codigo_a_buscar = input("Código IATA: ").strip()
    vuelos_filtrados = []

    for vuelo in vuelos:
        if vuelo['origen'] == codigo_a_buscar or vuelo['destino'] == codigo_a_buscar:
            vuelos_filtrados.append(vuelo)
        
    if vuelos_filtrados:
        print(Fore.MAGENTA + f"Estos son los vuelos con el código: {codigo_a_buscar}")
        for i in vuelos_filtrados:
            print(Fore.YELLOW + f"{i['origen']} => {i['destino']} -- Km: {i['km']}")

    else:
        print(f"No se encontraron vuelos con el código {codigo_a_buscar}")


# Funciones opcionales

# Terminado
def editar_eliminar_vuelos(vuelos):

    for n, i in enumerate(vuelos):
        print(Fore.YELLOW + f"{n}. {i['origen']} => {i['destino']} -- KM: {i['km']}")




    editar = input("¿Que quieres hacer, editar o eliminar?: ").lower()
    if editar == "eliminar":    # Opcion elegida = opción
        vuelo_a_eliminar = int(input("¿Que vuelo quieres eliminar?: "))
        if 0 <= vuelo_a_eliminar < len(vuelos): # Verifica si el numero que ha dado esta dentro de el numero de indices que hay
            del vuelos[vuelo_a_eliminar]
            print(Fore.GREEN + f"El vuelo de a se ha eliminado correctamente")
            for n, i in enumerate(vuelos):
                print(Fore.YELLOW + f"{n}. {i['origen']} => {i['destino']} -- KM: {i['km']}")

        else:
            print(Fore.RED + "Índice no válido")
    elif editar == "editar":    # Opcion elegida = editar
        vuelo_a_editar = int(input("¿Que vuelo quieres editar?: "))
        if 0 <= vuelo_a_editar < len(vuelos): # Verifica si el numero que ha dado esta dentro de el numero de indices que hay
            origen_o_destino = input("¿Origen o destino?: ").lower()

            if origen_o_destino == "origen": # Detecta que parte del vuelo quiere editar Origen/Destino
                while True:
                    origen_nuevo = input("Codigo IATA del nuevo origen: ")
                    if origen_nuevo.isupper() and len(origen_nuevo) == 3 and origen_nuevo.isalpha():# Verifica si el código que ha dado el usuario cumple los requisitos del codigo IATA
                        vuelos[vuelo_a_editar]['origen'] = origen_nuevo
                        print(Fore.CYAN + "Lista de vuelos actualizada: ")
                        break
                    else:
                        print(Fore.RED + "Error: El codigo debe de estar en mayusculas y contener 3 letras")

                for n, i in enumerate(vuelos):
                    print(Fore.YELLOW + f"{n}. {i['origen']} => {i['destino']} -- KM: {i['km']}")

            
            elif origen_o_destino == "destino":
                while True:
                    destino_nuevo = input("Codigo IATA del nuevo destino: ")
                    if destino_nuevo.isupper() and len(destino_nuevo) == 3 and destino_nuevo.isalpha(): #Verifica si el código que ha dado el usuario cumple los requisitos del codigo IATA
                        vuelos[vuelo_a_editar]['destino'] = destino_nuevo
                        print(Fore.CYAN + "Lista de vuelos actualizadas: ")
                        break
                    else:
                        print(Fore.RED + "Error: El codigo debe de estar en mayusculas y contener 3 letras")
                
                for n, i in enumerate(vuelos):
                    print(Fore.YELLOW + f"{n}. {i['origen']} => {i['destino']} -- KM: {i['km']}")


# Terminado
def guardar_datos(aeropuertos, vuelos, archivo="datos.json"):
    datos = {
        "aeropuertos": aeropuertos,
        "vuelos": vuelos
    }
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

#Terminado
def cargar_datos(archivo="datos.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            return datos.get("aeropuertos", []), datos.get("vuelos", [])
    except FileNotFoundError:
        return [], []
