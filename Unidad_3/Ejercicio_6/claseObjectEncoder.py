"""Ejercicio 6 - Unidad 3 / Ary Toro"""
import json
from pathlib import Path
from claseListaCalefactores import Lista,CalefactorGas,CalefactorElectrico

class ObjectEncoder:
    def decodificarDiccionario(self,d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Lista':
                calefactores=d['calefactores']
                dCalefactor=calefactores[0]
                lista=class_()
                for i in range(len(calefactores)):
                    dCalefactor=calefactores[i]
                    class_name=dCalefactor.pop('__class__')
                    class_=eval(class_name)
                    atributos=dCalefactor['__atributos__']
                    unCalefactor=class_(**atributos)
                    lista.agregarElemento(unCalefactor)
        return lista

    def guardarJSONArchivo(self,diccionario,archivo):
        with Path(archivo).open("w",encoding="UTF-8") as destino:
            json.dump(diccionario,destino,indent=4)
            destino.close()

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self,texto):
        return json.loads(texto)
