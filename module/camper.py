from os import system
import json
from .validate import menuNoValid
from .data import camper, generos

def save():
    info = {
        "Nombre": input("Ingrese el nombre del camper\n"),
        "Apellido": input("Ingrese el apellido del camper\n"),
        "Edad": int(input("Ingrese la edad del camper\n")),
        "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
    }
    camper.append(info)
    with open("module/storage/camper.json", "w") as f:
        data = json.dumps(camper, indent=4)
        f.write(data)
        f.close()
    return "Sucessfully Camper"

def edit():
    return "Edit to camper"

def search():
    print(camper)
    return "The camper is available"

def delete():
    return "Camper deleted"

def menu():
    bandera=True
    while (bandera):
        print("CRUD del camper")
        print("\t1. Guardar camper")
        print("\t2. Buscar camper")
        print("\t3. Actualizar camper")
        print("\t4. Eliminar camper")
        print("\t0. Atras")
        opc = int(input())
        match(opc):
            case 1:
                save()
            case 2:
                search()
            case 0:
                system("clear")
                bandera = False
            case _:
                menuNoValid(opc)