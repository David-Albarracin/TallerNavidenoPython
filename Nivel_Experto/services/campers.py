import services.corefile as db
import templates.menus as menu
import templates.reusable as reusable
import services.campusland as campus

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
    "notas":{}
    
}


status = ["aprobado", "no_aprobado", "estudiante", "entrevistas", "contratado"]

def newCamper():
    loadCampers()
    while True:
        menu.showHeader("registrar")
        cc = notRepetCC()
        if cc:
            camper["cc"] = cc
            camper["nombre"] = reusable.checkInput("str", f"Ingresa el Nombre del Camper")
            camper["apellidos"] = reusable.checkInput("str", f"Ingresa los Apellidos del Camper")       
            camper["direccion"] = reusable.checkInput("str", f"Ingresa la Direccion de residencia")   
            camper["telefono"]["celular"] = reusable.checkInput("str", f"Ingresa el Numero Celular del camper")
            camper["telefono"]["fijo"] = reusable.checkInput("str", f"Ingresa el Numero Fijo del camper")
            camper["acudiente"] = reusable.checkInput("str", f"Nombre del Acudiente de {camper['nombre']}")
            campers.update({camper["cc"]:camper})
            db.newFile(**campers)
            reusable.showSuccess(f"Camper {camper['nombre']} Creado Correctamente")
        
        yes = reusable.yesORnot("Desea Registrar Otro Camper")
        if not yes:
            break

def notRepetCC():
    while (True):
        cc = reusable.checkInput("str", f"Ingresa la Cedula de Ciudadanida del camper")
        if (cc in campers):
            reusable.showError("Error el Usuario ya esta registrado")
            return False
        else:
            return cc
        
def getCamper():
    loadCampers()
    cc = reusable.checkInput("str", f"Ingresa la Cedula de Ciudadanida del camper")
    return campers.get(cc)



def matricular():
    while(True):
        menu.showHeader("matricula")
        camper = getCamper()
        if camper:
            if (camper["estado"] == "aprobado"):
                campus.loadCampuslanDB()
                menu.showHeader("rutas1")
                rutas = campus.campuslandDB.get("rutas")
                reusable.printList(list(rutas.keys()))
                opcion = reusable.checkInput("str", "Ingresa el Nombre de la Ruta")
                if opcion in rutas:
                    ruta = rutas.get(opcion)
                    grupos = rutas[opcion]["grupos"]
                    trainers = rutas[opcion]["trainers"]
                    while True:
                        print(f"Trainers Disponibles {ruta["trainers"]}")
                        trainer = reusable.checkInput("str", f"Ingresa El Nombre del Trainer Para Asigarle a {camper['nombre']}")
                        if trainer in trainers:
                            dataTrainer = campus.campuslandDB["trainers"][trainer]
                            while True:
                                print(f"Grupos Disponibles {ruta["grupos"]}")
                                grupo = reusable.checkInput("str", f"Ingresa El Nombre del Grupo Para Asigarle a {camper['nombre']}")
                                if (grupo in dataTrainer["grupos"]) and (grupo in ruta["grupos"]):
                                    dataGrupo = campus.campuslandDB.get("grupos").get(grupo)
                                    if len(dataGrupo) <= 33:
                                        camper.update({"ruta": ruta["nombreRuta"]})
                                        camper.update({"trainer": trainer})
                                        camper.update({"grupo": grupo})
                                        camper.update({"estado": "estudiando"})
                                        dataGrupo.append(camper["cc"])
                                        db.updateDataBases()
                                        reusable.showSuccess("Se Matriculo Correctamente")
                                        return
                                    else:
                                        reusable.showError(f"{ruta['nombreRuta']} Llego al Maximo de Campers")
                                        return
                                else:
                                    reusable.showError(f"Ingresa el Grupo del Trainer {dataTrainer['nombre'].upper()}")
                        else:
                            reusable.showError("Ingresa el Nombre del Trainer Correctamente")
                else:
                    reusable.showError("Esta Ruta No Exite Ingresa Datos Reales")
            else:
                reusable.showInfo("El Estado del Camper No es Valido Para Esta Opcion")
        else:
            reusable.showInfo(f"No se Encontro al Camper")

        if not reusable.yesORnot("Desea Intentar Con Otro Camper"):
            break

    

URL = "campers.json"

def loadCampers():
    db.URL = URL
    campers.update(db.checkFile(**campers))