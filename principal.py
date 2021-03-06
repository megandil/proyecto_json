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
    if menus == 3:
        menuprocesador=menuprocesadores()
        print(menuprocesador)
        while menuprocesador != 7:
            if menuprocesador == 1:
                procesador="64-bit Intel Xeon Processor 2.80 GHz, 1M Cache, 800 MHz FSB"
            if menuprocesador == 2:
                procesador="Intel Celeron M Processor ULV 353 (512K Cache, 900 MHz, 400 MHz FSB)"
            if menuprocesador == 3:
                procesador="Intel Celeron Processor E3500 (1M Cache, 2.70 GHz, 800 MHz FSB)"
            if menuprocesador == 4:
                procesador="Intel Core2 Duo Processor SU7300 (3M Cache, 1.30 GHz, 800 MHz FSB)"
            if menuprocesador == 5:
                procesador="Intel Pentium Processor E5500 (2M Cache, 2.80 GHz, 800 MHz FSB)"
            if menuprocesador == 6:
                procesador=input("Introduce el nombre del procesador manualmente: ")
            print("----CARACTERÍSTICAS----")
            for clave,valor in buscaprocesador(procesador).items():
                print(clave,"->",valor) 
            menuprocesador=menuprocesadores()
            print(menuprocesador)
    if menus == 4:
        menusocket=sockets()
        print(menusocket)    
        while menusocket != 7:
            if menusocket == 1:
                socket="PPGA604"
            if menusocket == 2:
                socket="H-PBGA479"
            if menusocket == 3:
                socket="PBGA479"
            if menusocket == 4:
                socket="PPGA370"
            if menusocket == 5:
                socket="LGA775"
            if menusocket == 6:
                socket=input("Introduce el nombre del socket manualmente: ")
            print()
            print("---PROCESADORES COMPATIBLES---")
            for i in buscasocket(socket):
                print("-",i)
            print()  
            menusocket=sockets()
            print(menusocket)
    if menus == 5:
        numcore=input("Introduce el número de cores: ")
        menucaracteristica=menucaracteristicas()
        print(menucaracteristica)
        while menucaracteristica != 5:
            if menucaracteristica == 1:
                caracteristica="Processor Base Frequency"
                break
            if menucaracteristica == 2:
                caracteristica="Cache"
                break
            if menucaracteristica == 3:
                caracteristica="Bus Speed"
                break
            if menucaracteristica == 4:
                caracteristica="TDP"
                break
        print()
        print("---PROCESADORES---")
        for i in mayorcores(numcore):
            print("-",i)
            print("     ",caracteristica,"->",adicional(caracteristica,i))
        print()      
    menus=menu()
    print(menus)