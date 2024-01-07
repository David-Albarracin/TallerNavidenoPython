

import services.corefile as db
import templates.reusable as reusable
import templates.menus as menu

campuslandDB = {
    "areas":{
        "artemis":{
            "grupos":[]
        },
        "sputnik":{
            "grupos":[]
        },
        "apolo":{
            "grupos":[]
        }
    },

    "rutas": {
        "nodeJS":{
            "nombreRuta": "nodeJS",
            "area": "",
            "fechaInicio": "",
            "fechaFinal": "",
            "trainers": [],
            "grupo": "",
            "campers": [],
            "jornada": "",
            "fundamentosProgramacion": ["Introducción a la algoritmia", "PSeInt"],
            "programacionWEB": ["HTML","Bootstrap"],
            "programacionFormal": ["JavaScript", "C#"],
            "basesDatos": ["MongoDB", "MySql"],
            "backend": ["NodeJS", "Express"]
        },
        "java":{
            "nombreRuta": "java",
            "area": "",
            "fechaInicio": "",
            "fechaFinal": "",
            "trainers": [],
            "grupo": "",
            "campers": [],
            "jornada": "",
            "fundamentosProgramacion": ["Introducción a la algoritmia", "PSeInt"],
            "programacionWEB": ["HTML","CSS"],
            "programacionFormal": ["Java", "C#"],
            "basesDatos": ["Postgresql", "MySql"],
            "backend": ["Spring Boot", "Express"]
        },
        "netCore":{
            "nombreRuta": "netCore",
            "area": "",
            "fechaInicio": "",
            "fechaFinal": "",
            "trainers": [],
            "grupo": "",
            "campers": [],
            "jornada": "",
            "fundamentosProgramacion": ["Introducción a la algoritmia", "PSeInt"],
            "programacionWEB": ["HTML","CSS"],
            "programacionFormal": ["Java", "C#"],
            "basesDatos": ["Postgresql", "MySql"],
            "backend": ["NetCore", "POO"]
        }
    },

    "trainers":{
        "1":{
            "uid": "",
            "nombre": "",
            "jornada": "",
            "grupos": []
        }
    }
}

def newArea():
    loadCampuslanDB()
    menu.showHeader("areas")
    areas = campuslandDB.get("areas")
    for i in areas.keys():
        print(f" {i.upper()} ")
    opcion = reusable.yesORnot("\nEstas Seguro que Desea Crear Nueva Area de Entrenamiento? ")
    if opcion:
        reusable.showInfo("Por el Momento Campus Solo Cuenta con 3 Areas Asignalas en el Menu de Administrar Rutas")
        """
        nombre = reusable.checkInput("str", "Ingresa el Nombre del Area")
        areas.update({nombre: {"grupos": []}})
        reusable.showSuccess("Area Creada Correctamente")
        db.newFile(**campuslandDB)
        """
    return

def newRuta():
    pass


def loadCampuslanDB():
    db.URL = "campusland.json"
    campuslandDB.update(db.checkFile(**campuslandDB))


