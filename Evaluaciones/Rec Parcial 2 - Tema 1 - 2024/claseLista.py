"""Recuperatorio Parcial 2 - Tema 1 - 2024 / Ary Toro"""
import csv
from claseNodo import Nodo
from claseHerramientaElectrica import HerramientaElectrica
from claseMaquinariaPesada import MaquinariaPesada

class Lista:
    __comienzo:Nodo
    __actual:Nodo
    __indice:int
    __tope:int

    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            equipo=self.__actual.getEquipo()
            self.__actual= self.__actual.getSiguiente()
            return equipo

    def agregarEquipo(self,nuevoEquipo):
        nuevoNodo=Nodo(nuevoEquipo)
        nuevoNodo.setSiguiente(self.__comienzo)
        self.__comienzo=nuevoNodo
        self.__actual=nuevoNodo
        self.__tope+=1

    def cargarEquipos(self):
        band=False
        archivo= open("equipos.csv")
        readear=csv.reader(archivo,delimiter=";")
        for fila in readear:
            if band is False:
                band= True
            else:
                if fila[0]=="E":
                    self.agregarEquipo(HerramientaElectrica(fila[1],fila[2],int(fila[3]),fila[4],fila[5],fila[6],float(fila[7]),int(fila[8]),fila[9]))
                elif fila[0]=="M":
                    self.agregarEquipo(MaquinariaPesada(fila[1],fila[2],int(fila[3]),fila[4],fila[5],fila[6],float(fila[7]),int(fila[8]),fila[9],float(fila[10])))
        archivo.close()

    def mostrar_tipo(self,indice):
        if indice>=0 and indice<self.__tope:
            aux=self.__comienzo
            for i in range(indice):
                aux=aux.getSiguiente()

            if isinstance(aux.getEquipo(),MaquinariaPesada):
                print(f"El equipo {aux.getEquipo().getModelo()} en la posicion {indice} es del tipo Maquinaria Pesada")
            elif isinstance(aux.getEquipo(),HerramientaElectrica):
                print(f"El equipo {aux.getEquipo().getModelo()} en la posicion {indice} es del tipo Herramienta Electrica")
        else:
            raise IndexError

    def mostrar_cantidad_HE_anio(self,anio):
        cont=0
        for unequipo in self:
            if isinstance(unequipo,HerramientaElectrica) and unequipo.getAnioFab()==anio:
                cont+=1
        print(f"La cantidad de herramientas electricas fabricadas en {anio} es: {cont}")


    def mostrar_cantidad_MP_capacidad(self,capacidad):
        cont=0
        for unequipo in self:
            if isinstance(unequipo,MaquinariaPesada) and unequipo.getCapacidad()<=capacidad:
                cont+=1
        print(f"La cantidad de Maquinarias Pesadas cuya capacidad es menor a igual a {capacidad} es: {cont}")

    def listar_datos_equipos(self):
        for unequipo in self:
            print(f"""
            ° Marca: {unequipo.getMarca()}
              Modelo: {unequipo.getModelo()}
              Anio de Fabricacion: {unequipo.getAnioFab()}
              Tipo de Combustible: {unequipo.getTipoComb()}
              Potencia: {unequipo.getPotencia()}
              Capacidad de Carga: {unequipo.getCapacidad()}
              Tarifa de Alquiler: {unequipo.getTarifaAlquilerTotal()}""")

    def listarCantidad(self):
        cont1=0
        cont2=0
        for unequipo in self:
            if isinstance(unequipo,MaquinariaPesada):
                cont1+=1
            elif isinstance(unequipo,HerramientaElectrica):
                cont2+=1
        print(f"Pesadas: {cont1} Electricas: {cont2}")