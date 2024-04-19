"""Ejercicio 3 / Unidad 2 - Ary Toro"""
import numpy as np

class GestorVentas:
    """Clase gestor de ventas"""
    __arreglo: np.ndarray

    def __init__(self):
        self.__arreglo= np.empty([5,7],dtype=float)

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
        min=9999999999999
        for i in range(5):
            for j in range(7):
                if self.__arreglo[i][j]<min:
                    min=self.__arreglo[i][j]
                    auxMin=i+1
        print("La sucursal con menos facturacion durante la semana fue la ",auxMin)

    def opcion5(self):
        """Metodo para la opcion 5"""
        acum=0
        for i in range(5):
            for j in range(7):
                acum+=self.__arreglo[i][j]
        print("El total acumulado por todas las sucursales durante la semana es ",acum)

def menu():
    """Menu de opciones"""
    op=int(input("""
                                 MENÚ DE OPCIONES
          [1] Ingresa dia, numero e importe. Acumular para ese dia y sucursal
          [2] Ingresa sucursal. Calcular su total de facturacion
          [3] Ingresa dia. Mostrar sucursal que mas facturó ese dia
          [4] Calcular sucursal con menos facturacion durante la semana
          [5] Calcular el total facturado por todas las sucursales
          [0] SALIR
          -> """))
    return op

def principal():
    """Main del Programa"""
    arreglo_ventas=GestorVentas()
    arreglo_ventas.test()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            d1=int(input("Ingresa el dia(1 a 7): "))
            n1=int(input("Ingresa la sucursal(1 a 5): "))
            i1=float(input("Ingresa el importe: "))
            arreglo_ventas.opcion1(d1,n1,i1)
        elif opcion==2:
            n2=int(input("Ingresa numero de sucursal: "))
            arreglo_ventas.opcion2(n2)
        elif opcion==3:
            d3=int(input("Ingresa el dia: "))
            arreglo_ventas.opcion3(d3)
        elif opcion==4:
            arreglo_ventas.opcion4()
        elif opcion==5:
            arreglo_ventas.opcion5()
        else:
            print("Opcion no valida")
        opcion=menu()

if __name__=='__main__':
    principal()

"""Lote de prueba. (copiar todo y al ejecutar pegarlo)
250
650.5
130
0
210
100
810
330
410
110
50.6
710
301
800.9
231
74
23
600
310
1000
1300
340
610
140.3
781
620
630
110
670
210
630
270.5
3000
120
500
"""
