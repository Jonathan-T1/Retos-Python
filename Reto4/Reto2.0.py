op = 1
instructores2557861 = {}

def agregarModificar():

        inst = input("Ingrese el nombre del instructor: \n")
        inst = inst.lower()
        if inst in instructores2557861:
            print("El instructor ya se encuentra registrado en la ficha.")
            opcion1 = int(input("Digite 1 si desea modificar nombre del instructor. \nDigite 2 si desea modificar la materia del instructor de la ficha. \nDigite 3 si desea modificar el teléfono del instructor. \n"))
            if opcion1 == 1:
                nombre = input("Ingrese el nuevo nombre del instructor. \n")
                instructores2557861 ['Nombre'] = nombre
                print(instructores2557861)
            elif opcion1 == 2:
                materia = input("Ingrese la nueva materia del instructor. \n")
                instructores2557861 [inst]['Materia'] = materia
                print(instructores2557861)
            elif opcion1 == 3:
                telefono = int(input("Ingrese el nuevo teléfono del instructor. \n"))
                instructores2557861 [inst]['Teléfono'] = telefono
                print(instructores2557861)
            else:
                print("¡¡ERROR!! Opción no valida.")
        
        else:
            print("El instructor no se encuentra en el sistema.")
            instructores2557861[inst] = {}
            materia = input("Ingrese la materia del instructor. \n")
            instructores2557861[inst]['Materia'] = materia
            telefono = int(input("Ingrese el teléfono del instructor. \n"))
            instructores2557861[inst]['Telefono'] = telefono
            print(instructores2557861)

def buscar():

        inst = input("Ingrese el nombre del instructor que desea buscar: ")
        inst = inst.lower()
        print("Se encontraron los siguientes resultados:")
        for inst, datos in instructores2557861.items():
            if inst.startswith(inst):
                print(inst)
                print(f"Materia: {instructores2557861[inst]['Materia']} \nNúmero de teléfono: {instructores2557861[inst]['Telefono']}")
            else:
                print("No se encontro ningun instructor con ese nombre.")

def borrar():
    
        nombre = input("Ingrese el nombre del intructor que desea borrar: ")
        nombre = nombre.lower()
        if nombre in instructores2557861:
            print("Se encontraron los siguientes resultados: ")
            print(f"{instructores2557861}")
            borrar = int(input("Digite 1 para borrar el instructor. \nDigite 2 para cancelar la acción. \n"))
            if borrar == 1:
                del instructores2557861[nombre]
                print(f"El instructor {nombre} ha sido eliminado.")
                print(instructores2557861)
            elif borrar == 2:
                print("Usted ha cancelado la acción.")
                print(instructores2557861)
            else:
                print(f"El instructor {nombre} no existe en el diccionario.")

def listar():
    for x in instructores2557861:
        print(f"Los instructores registrados son {x} con la materia {instructores2557861[x]['Materia']} y un número de telefono {instructores2557861[x]['Telefono']}")

while op == 1:
    print("¡¡Bienvenido!!")
    print("1. Añadir/Modificar.")
    print("2. Buscar.")
    print("3. Borrar.")
    print("4. Listar.")
    print("5. Salir")
    opcion = int(input("Elija una opcion: "))

    if opcion == 1:
        agregarModificar()
    elif opcion == 2:
        buscar()
    elif opcion == 3:
        borrar()
    elif opcion == 4:
        listar()
    elif opcion == 5:
        print("Gracias por usar nuestros servicios.")
        break

    op = int(input("1. Para seguir modificando el diccionario. \n2. Para salir. \n"))