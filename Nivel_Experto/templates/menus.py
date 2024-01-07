import os


headers = {
    "home": "campuslands sistema de notas",
    "registar": "registar o editar camper",
    
}


opcions = {
    "home" : [
        "registrar camper",
        "registro de prueba de admision",
        "registro de area de entrenamiento",
        "registro de ruta de entrenamiento",
        "asignar camper a una ruta",
        "registar notas",
        "gestionar matricula",
        "editar trainer",
        "salir"
    ]

}


def showMenu(typeMenu):
    os.system("cls")
    headerT = f"+  {headers[typeMenu].upper()}  +"
    lenHeader = len(headerT)
    print("+"*lenHeader)
    print(headerT)
    print("+"*lenHeader)
    print("")
    for i, item in enumerate(opcions[typeMenu]):
        print(f" {i+1}.{item.capitalize()}")
    print("")
    return ":> "



