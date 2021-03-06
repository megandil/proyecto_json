import json
from funciones import *
with open("/home/usuario/Documentos/proyectolm/json/proyecto_json/intelcpu.json") as fichero:
    datos=json.load(fichero)
#print(datos)
menus=menu()
print(menus)
while menus != 6:
    if menus == 1:
        print("--------PROCESADORES--------")
        for i in nombreprocesadores():
            print("-",i)
        print()
    menus=menu()
    print(menus)
