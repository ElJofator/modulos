from os import system
import module.validate as validate
def menu():
    bandera = True
    system("clear")
    while(bandera):
        print("CRUD del Trainer")
        print("\t1. Guardar Trainer")
        print("\t2. Buscar Trainer")
        print("\t3. Actualizar Trainer")
        print("\t4. Eliminar Trainer")
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
    return "Succesfully Trainer"

def edit():
    return "Edit to Trainer"

def search():
    return "The Trainer is avaliable"

def delete():
    return "Trainer deleted"