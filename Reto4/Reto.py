op = 1
instructores = []

def anadir():
    instructores.append(input("Ingrese el nombre de instructor que desea añadir: "))
    print(f"Se añadio un nuevo instructor a la lista \n{instructores}")

def modificar():
    for index, l in enumerate(instructores):
        print(index, l)
    modificar=int(input("Ingrese la posición del intructor que desea modificar: "))
    nuevo=input("Ingrese el nombre del instructor para modificar: ")
    instructores[modificar]=nuevo
    print(f"Se ha modificado la lista añadiendo al intructor@ {nuevo}\n{instructores}")


def borrar():
    print("1. Borrar instructor por su nombre.")
    print("2. Borrar un instructor por su posiición especifica.")
    print("3. Borrar el ultimo instructor de la lista.")
    print("4. Borrar toda la lista.")
    opcion=int(input("Elija una opción. "))

    if opcion == 1:
        print(instructores)
        nombre=input("Ingrese el nombre exacto del instructor que desea borrar: ")
        instructores.remove(nombre)
        if len(instructores) == 0:
            print("La lista quedo vacia.")
        else:
            print(instructores)
    elif opcion == 2:
        for index, l in enumerate(instructores):
            print(index, l)
        borrar=int(input("Digite la posicion del instructor que desea borrar: "))
        del instructores[borrar]
    elif opcion == 3:
        instructores.pop()
        print(instructores)
    elif opcion == 4:       
        instructores.clear()
        print(instructores)

def enlistar():
    if len(instructores) == 0:
        print("La lista se encuentra vacia.")
    else: 
        for index, l in enumerate(instructores):
            print(index, l)

def buscar():
    nombre=input("Ingrese el nombre del instructor que desea buscar: ")
    nombre = nombre.lower()
    encontrado = False
    for nombre1 in instructores:
        nombre1 = nombre1.lower()
        if nombre1 == nombre:
            encontrado = True
            break
    if encontrado:
        print(f"El intructor {nombre}, fue encontrado en la lista.")
    else:
        print(f"El instructor {nombre}, no fue encontrado en la lista.") 

def ordenar():  
    instructores.sort()
    print(instructores)

while op == 1:

    print("Menu  de opciones.")
    print("1. Añadir instructor.")
    print("2. Modificar instructor.")
    print("3. Borrar instructor.")
    print("4. Enlistar.")
    print("5. Buscar instructor.")
    print("6. Ordenar la lista.")
    print("7. Salir.")
    opcion1 = int(input("Elija una opción. "))

    if opcion1 == 1:
        anadir()

    elif opcion1 == 2:
        modificar()

    elif opcion1 == 3:
        borrar()

    elif opcion1 == 4:
        enlistar()

    elif opcion1 == 5:
        buscar()

    elif opcion1 == 6:
        ordenar()

    elif opcion1 == 7:
        print("Gracias por usar nuestros servicios.")
    
    op = int(input("1. Para seguir modificando la lista.\n2. Para salir.\n"))