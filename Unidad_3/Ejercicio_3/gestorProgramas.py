"""Ejercicio 3 / Unidad 3 - Ary Toro"""
import csv
from claseProgramaCapacitacion import ProgramaCapacitacion
class GestorDeProgramas:
    __listaProgramas:list

    def __init__(self):
        self.__listaProgramas=[]

    def agregarPrograma(self,unprograma):
        self.__listaProgramas.append(unprograma)
        
    def cargarProgramas(self):
        band=False
        archivo=open("datosCursos.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if band is False:
                band=True
            else:
                self.agregarPrograma(ProgramaCapacitacion(fila[0],fila[1],int(fila[2])))
        archivo.close()

    def getCantidadProgramas(self):
        return len(self.__listaProgramas)

    def getProgramaPorIndice(self,pos):
        return self.__listaProgramas[pos]

    def mostrarEmpleadosDePrograma(self,xnom):
        band=False
        i=0
        while band is False and i<len(self.__listaProgramas):
            if self.__listaProgramas[i].getNombre()==xnom:
                self.__listaProgramas[i].listarEmpleados()
                band=True
            else:
                i+=1
        assert band is True
