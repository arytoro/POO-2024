"""Ejercicio 3 / Unidad 2 - Ary Toro"""
from gestorDeVentas import GestorVentas

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

if __name__=='__main__':
    ventas=GestorVentas()
    ventas.test()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            d1=int(input("Ingresa el dia(1 a 7): "))
            n1=int(input("Ingresa la sucursal(1 a 5): "))
            i1=float(input("Ingresa el importe: "))
            ventas.opcion1(d1,n1,i1)
        elif opcion==2:
            n2=int(input("Ingresa numero de sucursal(1 a 5): "))
            ventas.opcion2(n2)
        elif opcion==3:
            d3=int(input("Ingresa el dia(1 a 7): "))
            ventas.opcion3(d3)
        elif opcion==4:
            ventas.opcion4()
        elif opcion==5:
            ventas.opcion5()
        else:
            print("Opcion no valida")
        opcion=menu()

"""Lote de prueba.  Copiar todo y al ejecutar pegarlo
250
650.5
130
0
210
100
810
0
10
110
50.6
70
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