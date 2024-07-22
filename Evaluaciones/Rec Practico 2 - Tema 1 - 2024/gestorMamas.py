"""Recuperatio Practico 2 - Tema 1 - 2024 / Ary Toro"""
import csv
import numpy as np
from claseMadre import Madre
class GestorDeMamas:
    __cantidad:int
    __dimension:int
    __incremento:int
    __arregloMadres: np.ndarray

    def __init__(self):
        self.__cantidad=0
        self.__dimension=17
        self.__incremento=5
        self.__arregloMadres=np.empty(self.__dimension,dtype=Madre)

    def agregarMadre(self,unamadre):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arregloMadres.resize(self.__dimension)
        self.__arregloMadres[self.__cantidad]=unamadre
        self.__cantidad+=1

    def cargarMadres(self):
        band=True
        archivo=open('Mamas.csv')
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if band is True:
                band=False
            else:
                self.agregarMadre(Madre(int(fila[0]),int(fila[1]),fila[2]))
        archivo.close()

    def mostrar_datos_mama(self,xdni,GN):
        band=False
        i=0
        while band is False and i<self.__cantidad:
            if self.__arregloMadres[i].getDNI()==xdni:
                m=self.__arregloMadres[i]
                print(f"""
                      °Apellido y Nombre: {m.getAyN()}
                      Edad: {m.getEdad()}
                      Tipo de Parto: {GN.getTipo_porDNI(xdni)}
                      Bebé/s:""")
                GN.listarBebes_porDNI(xdni)
                band=True
            else:
                i+=1
        assert band is True

    def listar_mamas_partos_multiples(self,xdni):
        band=False
        i=0
        while band is False and i<self.__cantidad:
            if self.__arregloMadres[i].getDNI()==xdni:
                print(f"""
                    °Apellido y Nombre: {self.__arregloMadres[i].getAyN()}
                    Edad: {self.__arregloMadres[i].getEdad()}
                    DNI: {self.__arregloMadres[i].getDNI()}""")
                band=True
            else:
                i+=1
