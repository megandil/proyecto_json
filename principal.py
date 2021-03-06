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
    if menus == 2:
        cuenta=contarprocesadores()
        print("---64 BITS---")
        print("%i procesadores" % cuenta[0])
        print()
        print("---32 BITS---")
        print("%i procesadores" % cuenta[1])
        print()
    menus=menu()
    print(menus)
