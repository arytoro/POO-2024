"""Ejercicio 3 / Unidad 3 - Ary Toro"""
import csv
from random import choice
from claseEmpleado import Empleado
class GestorEmpleados:
    __listaEmpleados:list

    def __init__(self):
        self.__listaEmpleados=[]

    def agregarEmpleado(self,unempleado):
        self.__listaEmpleados.append(unempleado)
        
    def cargarEmpleados(self):
        band=False
        archivo=open("datosEmpleados.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if band is False:
                band=True
            else:
                self.agregarEmpleado(Empleado(fila[0],int(fila[1]),fila[2]))
        archivo.close()

    def getCantidadEmpleados(self):
        return len(self.__listaEmpleados)

    def getEmpleadoPorIndice(self,pos):
        return self.__listaEmpleados[pos]
            
    def mostrarDuracionDeProgramasEmpleado(self,xid):
        band= False
        i=0
        while band is False and i<len(self.__listaEmpleados):
            if self.__listaEmpleados[i].getID()==xid:
                self.__listaEmpleados[i].listarDuracionProgramas()
                band=True
            else:
                i+=1
        assert band is True

    def mostrarEmpleadosSinMatriculas(self):
        band=False
        for unempleado in self.__listaEmpleados:
            if unempleado.getCantidadMatriculas()==0:
                print(unempleado)
                band=True
        assert band is True

    def mostrarIDSmatriculas(self):
        cont=0
        for unempleado in self.__listaEmpleados:
            print("Matriculas de empleado ",cont+1)
            unempleado.listarIDSEmpleado()
            cont+=1
