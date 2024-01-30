from os import system
import module.validate as validate
def menu():
    bandera = True
    system("clear")
    while(bandera):
        print("CRUD del Camper")
        print("\t1. Guardar Camper")
        print("\t2. Buscar Camper")
        print("\t3. Actualizar Camper")
        print("\t4. Eliminar Camper")
        print("\t0. Salir")
        opc = input()
        match(opc):
            case "1":
                save()
            case "2":
                search()
            case "3":
                edit()
            case "4":
                delete()
            case "0":
                bandera = False
            case _:
                validate.menuNoVAlid(opc)

def save():
    info = {
        "Nombre": input("Ingrese el nombre del camper\n"),
        "Apellido": input("Ingrese el apellido del camper\n"),
        "Edad": int(input("Ingrese la edad del camper\n")),
        "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
    }
    camper.append(info)
    return "Sucessfully Camper"

def edit():
    return "Edit to Camper"

def search():
    return "The Camper is avaliable"

def delete():
    return "Camper deleted"