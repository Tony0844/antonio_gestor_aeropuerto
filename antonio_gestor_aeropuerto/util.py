import os
import json
from colorama import init, Fore, Style
from time import sleep

init(autoreset=True)

aeropuertos =[] 

vuelos = [
    {"origen":"madrid","destino": "barcelona","id": "IB101", "km": 504, "plazas": 180}, #Madrid => Barcelona -- 1
    {"origen": "barcelona","destino": "malaga", "id": "VY450", "km": 770, "plazas": 160}, #Barcelona => Malaga -- 2
    {"origen": "malaga","destino": "madrid", "id": "UX333", "km": 430, "plazas": 220} #Malaga => Madrid -- 3

]

km_1 = vuelos[0]['km']
plazas_1 = vuelos[0]['plazas']


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
