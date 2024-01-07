import services.corefile as db
import templates.menus as menu
import templates.reusable as reusable

db.URL = "campers.json"

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
    campers.update(db.checkFile(**campers))
    camper["cc"] = notRepetCC()
    for key, value in camper.items():
        if not value:
            camper[key] = reusable.checkInput((type(value)), f"Ingresa {key.upper()} del camper")

    camper["telefono"]["celular"] = reusable.checkInput("str", f"Ingresa el Numero Celular del camper")
    camper["telefono"]["fijo"] = reusable.checkInput("str", f"Ingresa el Numero Fijo del camper")
    camper["acudiente"] = reusable.checkInput("str", f"Nombre del Acudiente de {camper['nombre']}")
    campers.update({camper["cc"]:camper})
    db.updateFile(**campers)
    reusable.showSuccess(f"Camper {camper['nombre']} Creado Correctamente")

def notRepetCC():
    while (True):
        cc = reusable.checkInput("str", f"Ingresa la Cedula de Ciudadanida del camper")
        if (cc in campers):
            reusable.showError("Error el Usuario ya esta registrado")
        else:
            return cc
        
def getCamper():
    campers.update(db.checkFile(**campers))
    cc = reusable.checkInput("str", f"Ingresa la Cedula de Ciudadanida del camper")
    return campers.get(cc)
