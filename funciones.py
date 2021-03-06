import json
with open("/home/usuario/Documentos/proyectolm/json/proyecto_json/intelcpu.json") as fichero:
    datos=json.load(fichero)
def menu():
    print('''1.Muestra el nombre de los procesadores Intel.
2.Cuenta los procesadores de instrucción de 32 y 64 bits.
3.Muestra los datos más importantes(performance) de un código de procesador dado(los códigos serán mostrados y el usuario elige el que quiera).
4.Muestra el nombre de los procesadores de que tienen un socket especificado por el usuario.
5.Muestra el nombre de los procesadores en los que el número de cores sea mayor al que especifique el usuario, y además una característica opcional(el programa le dará un número de características y el usuario escogerá la que le convenga).
6.Salir''')
    opcion=int(input("Introduce la opcion:"))
    return opcion
def nombreprocesadores():
    procesadores=[]
    for i in datos.get("procesadores").get("procesador"):
        procesador=i.get("name")
        procesadores.append(procesador)
    return procesadores
def contarprocesadores():
    cuenta64=0
    cuenta32=0
    for i in datos.get("procesadores").get("procesador"):
        procesador=i.get("Advanced Technologies").get("Instruction Set")
        if procesador == "64-bit":
            cuenta64=cuenta64+1
        if procesador == "32-bit":
            cuenta32=cuenta32+1
    lista=[cuenta64,cuenta32]
    return lista
def menuprocesadores():
    print("------ALGUNOS PROCESADORES------")
    print('''1.Intel Xeon Processor 2.80 GHz
2.Intel Celeron M Processor ULV 353
3.Intel Celeron Processor E3500
4.Intel Core2 Duo Processor SU7300
5.Intel Pentium Processor E5500
6.Elegir otro
7.Salir''')
    opcion=int(input("Introduce la opcion:"))
    return opcion
def buscaprocesador(nombre):
    for i in datos.get("procesadores").get("procesador"):
        if i.get("name") == nombre:
            caracteristicas=i.get("Performance")
            return caracteristicas