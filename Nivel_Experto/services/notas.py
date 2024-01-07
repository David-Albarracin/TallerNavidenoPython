import services.campers as sc
import services.corefile as db
import templates.reusable as reusable



def pruebaAdmision():
    while(True):
        camper = sc.getCamper()
        if camper:
            nota = reusable.checkInput("float", f"Ingresa la nota de la prueba de admision de {camper["nombre"]}")
            if (nota >= 60):
                camper["estado"] = "aprobado"
            else:
                camper["estado"] = "no aprobado"
            reusable.showSuccess("Se Actualizo la Nota Correctamente")
        else:
            print("No se Encontro a el Camper")
        
        if(not reusable.yesORnot("Desea Registrar la Nota de otro Camper")):
                db.URL = "campers.json"
                db.updateFile(**sc.campers)
                break