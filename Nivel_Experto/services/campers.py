import services.corefile as db
import templates.menus as menu
import templates.reusable as reusable

campers = {}

camper = {
    "cc": "",
    "nombre": "",
    "apellido": "",
    "ciudad": "Bucaramanga",
    "direccion": "",
    "acudiente": ".",
    "telefono": {
        "celular": "",
        "fijo": ""
    },
    "estado": "inscrito",
    "ruta": {
        "uid": "",
        "moduloFundamentos": {
            "notaPruebaTecnica": 0,
            "notaPruebaTeorica": 0,
            "notasTrabajosQuizes": 0,
            "definitiva": 0
        }
    }
}

def newCamper():
    loadCampers()
    menu.showMenu("registrar")
    camper["cc"] = notRepetCC()
    camper["nombre"] = reusable.checkInput("str", f"Ingresa el Nombre del Camper")
    camper["apellidos"] = reusable.checkInput("str", f"Ingresa los Apellidos del Camper")       
    campers["direccion"] = reusable.checkInput("str", f"Ingresa la Direccion de residencia")   
    camper["telefono"]["celular"] = reusable.checkInput("str", f"Ingresa el Numero Celular del camper")
    camper["telefono"]["fijo"] = reusable.checkInput("str", f"Ingresa el Numero Fijo del camper")
    camper["acudiente"] = reusable.checkInput("str", f"Nombre del Acudiente de {camper['nombre']}")
    campers.update({camper["cc"]:camper})
    db.newFile(**campers)
    reusable.showSuccess(f"Camper {camper['nombre']} Creado Correctamente")

def notRepetCC():
    while (True):
        cc = reusable.checkInput("str", f"Ingresa la Cedula de Ciudadanida del camper")
        if (cc in campers):
            reusable.showError("Error el Usuario ya esta registrado")
        else:
            return cc
        
def getCamper():
    loadCampers()
    cc = reusable.checkInput("str", f"Ingresa la Cedula de Ciudadanida del camper")
    return campers.get(cc)


def loadCampers():
    db.URL = "campers.json"
    campers.update(db.checkFile(**campers))