from os import system
import module.camper as camper
import module.trainer as trainer
import module.validate as validate

def menu():
    print("Sistema de almacenamiento de datos para Campus")
    print("\t1. Información del camper")
    print("\t2. Información del trainer")
    print("\t0. Salir")
bandera = True
system("clear")
while(bandera):
    menu()
    opc = input()
    match(opc):
        case "1":
            camper.menu()
        case "2":
            trainer.menu()
        case "0":
            bandera = False
        case _:
            validate.menuNoVAlid(opc)