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