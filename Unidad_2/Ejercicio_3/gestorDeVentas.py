"""Ejercicio 3 / Unidad 2 - Ary Toro"""
import numpy as np

class GestorVentas:
    """Clase gestor de ventas"""
    __arreglo: np.ndarray

    def __init__(self):
        self.__arreglo= np.zeros([5,7],dtype=float) #Genero una matriz de 0s con 5 filas y 7 columnas que guardara reales

    def test(self):
        """Metodo para la instanciacion"""
        for i in range(5):
            print("--------------------------------------------------------")
            print(f"° Carga de Ventas para la sucursal {i+1}")
            for j in range(7):
                self.__arreglo[i][j]= float(input(f"Ingresa el importe para el dia {j+1}: "))

    def opcion1(self,dia,num,imp):
        """Metodo para la opcion 1"""
        self.__arreglo[num-1][dia-1]+=imp
        print("El nuevo importe es: ",self.__arreglo[num-1][dia-1])

    def opcion2(self,num):
        """Metodo para la opcion 2"""
        acum=0
        for i in range(7):
            acum+=self.__arreglo[num-1][i]
        print(f"El total recaudado por la sucursal {num} es: ",round(acum,2))

    def opcion3(self,dia):
        """Metodo para la opcion 3"""
        max=-1.5
        for i in range(5):
            if self.__arreglo[i][dia-1]>max:
                max=self.__arreglo[i][dia-1]
                auxMax=i+1
        print("La sucursal que mas facturo ese dia fue la ",auxMax)

    def opcion4(self):
        """Metodo para la opcion 4"""
        minR=9999999999999
        for i in range(5):
            acum=0
            for j in range(7):
                acum+=self.__arreglo[i][j]
            if acum<minR:
                minR=acum
                auxMin=i+1
        print("La sucursal con menos facturacion durante la semana fue la ",auxMin)

    def opcion5(self):
        """Metodo para la opcion 5"""
        acum=0
        for i in range(5):
            for j in range(7):
                acum+=self.__arreglo[i][j]
        print("El total acumulado por todas las sucursales durante la semana es ",acum)
