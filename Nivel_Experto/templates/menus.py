import os


headers = {
    "home": "campuslands sistema de notas",
    "registrar": "registar un nuevo camper",
    "areas": "areas disponibles"
    
}


opcions = {
    "home" : [
        "registrar camper",
        "registro de prueba de admision",
        "registro de area de entrenamiento",
        "registro de ruta de entrenamiento",
        "asignar camper a una ruta",
        "gestionar matricula",
        "registar notas",
        "registrar nuevo trainer",
        "salir"
    ],

}


def showMenu(typeMenu):
    showHeader(typeMenu)
    for i, item in enumerate(opcions[typeMenu]):
        print(f" {i+1}.{item.capitalize()}")
    print("")
    return ":> "


def showHeader(typeMenu):
    os.system("cls")
    headerT = f"+  {headers[typeMenu].upper()}  +"
    lenHeader = len(headerT)
    print("+"*lenHeader)
    print(headerT)
    print("+"*lenHeader)
    print("")
    return

