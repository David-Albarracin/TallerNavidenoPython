import json
import os


PATH = "./Nivel_Experto/db/"
URL = ""



def newFile(**kwargs):
    with open(f"{PATH}{URL}", "w") as archivo:
        json.dump(kwargs, archivo, indent=4)


def loadData():
    with open(f"{PATH}{URL}", "r") as archivo:
        return json.load(archivo)
    


def checkFile(**kwargs):
    if(os.path.isfile(f"{PATH}{URL}")):
        kwargs.update(loadData())
    else:
        newFile(**kwargs)

    return kwargs

"""
def updateFile(**kwargs):
    with open(f"{PATH}{URL}","r+") as archivo:
        data = json.load(archivo)
        data.update(kwargs)
        archivo.seek(0)
        json.dump(data,archivo,indent=4)
"""