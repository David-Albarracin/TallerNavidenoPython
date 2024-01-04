import reusable
import menusTemplate as menu

novatos = []
intermedio = []
avanzado = []


def regisCamper():
    while(True):
        print("Registrar Jugador en la Categoria")
        opMenu = input(menu.categorias)
        categoria = ""
        if(opMenu == "1"):
            categoria = "novatos"
        elif(opMenu == "2"):
            categoria = "intermedio"
        elif(opMenu == "3"):
            categoria = "avanzado"
        else:
            pass
        if categoria:
            nombre = input("Ingresa el Nombre del Camper :> ")
            while(True):
                edad = reusable.inputNumber(f"Ingresa la Edad del Camper {nombre}")
                if(edad == 15) or (edad == 16):
                    if categoria != "novatos":
                        print("la edad del participante no concide con su categoria")
                    else:
                        return
                elif(edad > 17) and (edad <=20):
                    if categoria != "principiante":
                        print("la edad del participante no concide con su categoria")
                    else:
                        break
                elif(edad > 20):
                    if categoria != "avanzado":
                        print("la edad del participante no concide con su categoria")
                    else:
                        break
                else:
                    print("Edad del participante no valida para el proceso")