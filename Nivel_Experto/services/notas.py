import services.campers as sc
import services.corefile as db
import templates.reusable as reusable



def pruebaAdmision():
    while(True):
        camper = sc.getCamper()
        if camper:
            if (camper["estado"] == "inscrito"):
                teorica = reusable.checkInput("float", f"Ingresa la nota de la prueba teorica {camper["nombre"]}")
                practica = reusable.checkInput("float", f"Ingresa la nota de la prueba practica {camper["nombre"]}")
                nota = (teorica + practica) / 2
                if (nota >= 60):
                    camper["estado"] = "aprobado"
                else:
                    camper["estado"] = "no_aprobado"

                reusable.showSuccess("Se Actualizo la Nota Correctamente")
                
            elif(camper["estado"] == "no_aprobado"):
                print(f"El Camper {camper["nombre"]} ya Presento las Pruebas y NO fue apto")
            elif(camper["estado"] == "aprobado"):
                print(f"El Camper {camper["nombre"]} ya Presento las Pruebas y Aprobo")
            else:
                print(f"El estado de {camper["nombre"]} no es apto para esta opcion")

        else:
            print("No se Encontro a el Camper")
        
        if(not reusable.yesORnot("Desea Registrar la Nota de otro Camper")):
                db.URL = "campers.json"
                db.newFile(**sc.campers)
                break