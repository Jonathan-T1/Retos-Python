op = 1
instructores=['Jennifer', 'Jonathan', 'Andres']
while op == 1:
    print(instructores)
    opciones=int(input("Digite 1 para agregar un instructor. \nDigite 2 para modificar a los instructore. \nDigite 3 para borrar un instructor. \nDigite 4 para enlistar un instructor. \nDigite 5 para buscar un instructor. \nDigite 6 para ordenar la lista alfabeticamente. \nDigite 7 para salir.\n"))
    if opciones == 1:
        instructores.append(input("Ingrese el nombre de instructor que desea añadir: "))
        print(f"Se añadio un nuevo instructor a la lista \n{instructores}")
    elif opciones == 2:
        for index, l in enumerate(instructores):
            print(index, l)
        modificar=int(input("Ingrese la posición del intructor que desea modificar: "))
        nuevo=input("Ingrese el nombre del instructor para modificar: ")
        instructores[modificar]=nuevo
        print(f"Se ha modificado la lista añadiendo al intructor@ {nuevo}\n{instructores}")
    elif opciones == 3:  
        opcion=int(input("Digite 1 para borrar un instructor por su nombre. \nDigite 2 para borrar un instructor por su posicion especifica en la lista. \nDigite 3 para borrar el ultimo instructor de la lista. \nDigite 4 para borrar toda la lista. \n"))
        if opcion == 1:
            instructores.remove(input("Ingrese el nombre del instructor que desea borrar"))
            print(instructores)
        elif opcion == 2:
            for index, l in enumerate(instructores):
                print(index, l)
            borrar=int(input("Digite la posicion del instructor que desea borrar: "))
            del instructores[borrar]
            print(instructores)
        elif opcion == 3:
            instructores.pop()
            print(instructores)
        elif opcion == 4:
            instructores.clear()
            print(instructores)
    elif opciones == 4:
        for index, l in enumerate(instructores):
            print(index, l)
    elif opciones == 5:
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
    elif opciones == 6:
        instructores.sort()
        print(instructores)
    elif opciones == 7:
        print("Gracias por usar nuestros servicios.")
        break
    else:
        print("Opcion no valida")
    op=int(input("Digite 1 si desea seguir modificando la lista. \nDigite 2 si desea salir. \n"))