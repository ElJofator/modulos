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
    return "Succesfully Camper"

def edit():
    return "Edit to Camper"

def search():
    return "The Camper is avaliable"

def delete():
    return "Camper deleted"