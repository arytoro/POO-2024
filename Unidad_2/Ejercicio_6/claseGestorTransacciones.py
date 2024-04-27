"""Ejercicio 6 - Unidad 2 / Ary Toro"""
import numpy as np
import csv
from claseTransaccion import Transaccion
class GestorTransacciones:
    """Clase del gestor de transacciones"""
    __transacciones: list
    def __init__(self):
        """Metodo constructor del gestor de transacciones"""
        self.__transacciones=[]

    def agregarTransaccion(self,unatransaccion):
        """Metodo para agregar una transaccion a la lista de transacciones"""
        self.__transacciones.append(unatransaccion)

    def test(self):
        """Metodo para leer transacciones desde archivo"""
        archivo= open('transaccionesBilletera.csv')
        reader= csv.reader(archivo,delimiter=';')
        band=True
        for fila in reader:
            if band is True:
                band=False
            else:
                self.agregarTransaccion(Transaccion(int(fila[0]),int(fila[1]),float(fila[2]),fila[3]))
        archivo.close()

    def getTransaccionesPorCVU(self,cvu):
        """Metodo que devuelve el importe total de todas las transacciones de ese CVU"""
        acumulador_importe=0
        for unatransaccion in self.__transacciones:
            if unatransaccion.getCVU()==cvu:
                acumulador_importe+=unatransaccion.getImporte()    
        return acumulador_importe

    def eliminarTransaccion(self,num):
        """Metodo que elimina una cuenta a partir del CVU"""
        i=0
        band=False
        long=len(self.__transacciones)
        while band is False and i<long:
            if num==self.__transacciones[i].getNumero():
                del self.__transacciones[i]
                band=True
            else:
                i+=1
        if band is False:
            print("No existe una transaccion con ese numero")
