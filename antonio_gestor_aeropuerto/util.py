import os
from colorama import init, Fore, Style
from time import sleep

init(autoreset=True)

aeropuertos = [
    {"codigo": "MAD", "nombre": "Aeropuerto Adolfo Suárez Madrid-Barajas", "ciudad": "Madrid"},
    {"codigo": "BCN", "nombre": "Aeropuerto Josep Tarradellas Barcelona-El Prat", "ciudad": "Barcelona"},
    {"codigo": "AGP", "nombre": "Aeropuerto de Málaga-Costa del Sol", "ciudad": "Málaga"},
    {"codigo": "SVQ", "nombre": "Aeropuerto de Sevilla", "ciudad": "Sevilla"}
]

vuelos = [
    {"origen": "MAD", "destino": "BCN"},
    {"origen": "AGP", "destino": "SVQ"},
    {"origen": "BCN", "destino": "MAD"},
    {"origen": "SVQ", "destino": "AGP"}
]


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
        else:
            print(Fore.RED + "Error: El código debe tener 3 letras en MAYÚSCULAS, no contener símbolos y no estar ya en la lista")
 
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

    vuelos.append({"origen": origen, "destino": destino, "km": None})
    print(Fore.GREEN + f"Vuelo añadido: {origen} → {destino} -- KM:{None}")

# Terminado    
def listar_vuelos(vuelos):
    
    for i,vuelo in enumerate(vuelos, start=1):
        print(Fore.YELLOW  + f"{i}.{vuelo['origen']} => {vuelo['destino']} -- KM:{None}")

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
            print(Fore.YELLOW + f"{i['origen']} => {i['destino']} -- Km: {None}")
    else:
        print(f"No se encontraron vuelos con el código {codigo_a_buscar}")


# Funciones opcionales

def editar_eliminar_vuelos(vuelos):
    for n,i in enumerate(vuelos):
        print(Fore.YELLOW  + f"{n}. {i['origen']} => {i['destino']} -- KM:{None}")


    editar = input("¿Que quieres hacer, editar o eliminar?: ").lower()
    if editar == "eliminar":
        vuelo_a_eliminar = int(input("¿Que vuelo quieres eliminar?: "))
        if 0 <= vuelo_a_eliminar < len(vuelos):
            del vuelos[vuelo_a_eliminar]
            for i in vuelos:
                print(Fore.YELLOW  + f"{n}. {i['origen']} => {i['destino']} -- KM:{None}")
        else:
            print(Fore.RED + "Índice no válido")
