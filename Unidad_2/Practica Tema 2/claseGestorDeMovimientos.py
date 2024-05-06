import csv
import numpy as np
from claseMovimiento import Movimiento

class GestorDeMovimientos:
    __cantidad:int
    __dimension:int
    __incremento:int
    __arregloMovimientos:np.ndarray

    def __init__(self):
        self.__cantidad=0
        self.__dimension=21
        self.__incremento=5
        self.__arregloMovimientos=np.empty(self.__dimension,dtype=Movimiento)

    def agregarMovimiento(self,unmovimiento):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arregloMovimientos.resize(self.__dimension)
        self.__arregloMovimientos[self.__cantidad]=unmovimiento
        self.__cantidad+=1

    def test(self):
        band:bool=False
        archivo=open("MovimientosAbril2024.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if band is False:
                band=True
            else:
                self.agregarMovimiento(Movimiento(int(fila[0]),fila[1],fila[2],fila[3],float(fila[4])))
        archivo.close()

    def existenMovimientos_porNumCuenta(self,numC):
        existe:bool=False
        i:int=0
        while i<self.__cantidad and existe is False:
            if self.__arregloMovimientos[i].getNumCuenta()==numC:
                existe=True
            else:
                i+=1
        return existe

    def ordenarMovimientos(self):
        self.__arregloMovimientos=np.sort(self.__arregloMovimientos)
        print("Los movimientos fueron ordenados por numeros de cuenta!")

    def listarMovimientos(self):
        for unmovimiento in self.__arregloMovimientos:
            print(unmovimiento)
