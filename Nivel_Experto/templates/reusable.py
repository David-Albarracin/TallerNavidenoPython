import os
import random


def checkInput(type, message):
    while (True):
        try:
            data = input(f"{message} :> ")
            if(type == "int"):
                data = int(data)
            elif(type == "float"):
                data = float(data)
        except ValueError:
            showError("Error al Ingresa el Dato Intentalo de Nuevo")
        else:
            if(type == "str") and (len(data) < 1):
                showError("Error al Ingresa el Dato Intenta Ingresar Datos Reales")
            else:
                return data
        

def showSuccess(message):
    os.system("cls")
    print("\033[92m{}\033[00m" .format(message))
    os.system("pause")


def showError(message):
    os.system("cls")
    print("\033[91m{}\033[00m" .format(message))
    os.system("pause")


def showInfo(message):
    os.system("cls")
    print("\033[93m{}\033[00m" .format(message))
    os.system("pause")


def uuid():
    return random.randint(0000, 9999)

def yesORnot(message):
    while(True):
        continuar = checkInput("str", f"{message} Si(s) o No(n)").lower()
        if continuar == "s":
            return True
        elif continuar == "n":
            return False
        else:
            showError("Error Opcion no Reconocida Ingresa s para (Si) o n Para (No)")