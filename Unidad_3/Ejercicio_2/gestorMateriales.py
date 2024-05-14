"""Ejercicio 2 / Unidad 3 - Ary Toro"""
import csv
from claseMaterialRefractario import MaterialRefractario

class GestorDeMateriales:
    __listaMateriales:list

    def __init__(self):
        self.__listaMateriales=[]

    def agregarMaterial(self,unmaterial):
        self.__listaMateriales.append(unmaterial)

    def cargarMateriales(self):
        band=False
        archivo=open("materiales.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if band is False:
                band=True
            else:
                self.agregarMaterial(MaterialRefractario(int(fila[0]),fila[1],float(fila[2]),float(fila[3])))
        archivo.close()

    def getTotalMateriales(self):
        return len(self.__listaMateriales)

    def getMaterialPorPosicion(self,pos):
        return self.__listaMateriales[pos]
