"""Ejercicio 1 / Unidad 3 - Ary Toro"""
import csv
from claseEdificio import Edificio

class GestorDeEdificios:
    __listaEdificios:list

    def __init__(self):
        self.__listaEdificios=[]

    def agregarEdificio(self,unedificio):
        self.__listaEdificios.append(unedificio)

    def cargarEdificios(self):
        archivo=open("EdificioNorte.csv")
        reader=csv.reader(archivo,delimiter=";")
        xedificio=None
        for fila in reader:
            if len(fila)==6:
                xedificio=Edificio(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]),int(fila[5]))
                self.agregarEdificio(xedificio)
            else:
                xedificio.agregarDepartamento(int(fila[0]),int(fila[1]),fila[2],int(fila[3]),int(fila[4]),int(fila[5]),int(fila[6]),float(fila[7]))
        archivo.close()

    def cantidadEdificios(self):
        print(len(self.__listaEdificios))

    def mostrarPropietarios(self,xnom):
        band = False
        i=0
        while band is False and i<len(self.__listaEdificios):
            if self.__listaEdificios[i].getNombreEdificio()==xnom:
                self.__listaEdificios[i].listarPropietariosDepartamentos()
                band=True
            else:
                i+=1
        return band

    def mostrarSuperficieTotalEdificio(self,xid):
        band = False
        i=0
        while band is False and i<len(self.__listaEdificios):
            if self.__listaEdificios[i].getIdEdificio()==xid:
                print("La superficie total cubierta es: ",self.__listaEdificios[i].getSuperficieTotal())
                band=True
            else:
                i+=1
        return band

    def mostrarSuperficieTotalDepartamento(self,xnom):
        band=False
        for unedificio in self.__listaEdificios:
            if unedificio.existePropietario(xnom) is True:
                print(f"Es propietario de departamento/s en el edificio {unedificio.getIdEdificio()}")
                print(f"La superficie total de dichos deptos es {unedificio.getSuperficieDeptosPropietario(xnom)}")
                print(f"Que representa el %{round((unedificio.getSuperficieDeptosPropietario(xnom)*100)/unedificio.getSuperficieTotal(),2)} de la superficie total del edificio\n")
                band=True
        return band

    def mostrarDepartamentosConCondiciones(self,xnumP):
        band= False
        for unedificio in self.__listaEdificios:
            if unedificio.existeNumPiso(xnumP) is True:
                cantidad=unedificio.listarDepartamentosConCondiciones(xnumP)
                print(f"\nPor lo tanto {cantidad} departamentos cumplen esas condiciones en el edificio {unedificio.getIdEdificio()}\n")
                band=True
        return band
                