"""Ejercicio 4 / Unidad 2 - Ary Toro"""
from GestorMotos import GestorDeMotos
from GestorPedidos import GestorDePedido

def menu():
    """Menu de opciones"""
    op=int(input("""
                                 MENÚ DE OPCIONES
          [1] Leer datos de motos desde archivo csv
          [2] Leer datos de pedidos desde archivo csv
          [3] Cargar nuevo pedido
          [4] Modificar tiempo real de entrega
          [5] Mostrar datos de conductor y promedio de tiempo real de entrega
          [6] Mostrar comisiones de cada moto
          [0] SALIR
          -> """))
    return op

if __name__=='__main__':
    #Recuerdo que todos los pedidos tienen tiempo de entrega real en 0 por defecto
    #Si se quiere modificar se debe usar la opcion 4 (sino se modifica afectara el promedio de la op 5)
    #Te recomiendo usar la opcion 6 para ver los datos precargados y las modificaciones que hagas
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            motos=GestorDeMotos()
            motos.testMoto()
            l_patentes=motos.patentesRegistradas()#Esta lista contiene todas las patentes
            l_conductores=motos.conductoresRegistrados()#Esta lista tiene los nombres de todos los conductoes
            print('Operacion 1 Exitosa')
        elif opcion==2:
            pedidos=GestorDePedido()
            pedidos.testPedido()
            pedidos.ordenar()
            print('Operacion 2 Exitosa')
        elif opcion==3:
            pedidos.nuevoPedido(l_patentes)
            pedidos.ordenar()
        elif opcion==4:
            pedidos.modificarTiempoReal()
        elif opcion==5:
            pedidos.mostrarDatosyProm(motos)
        elif opcion==6:
            pedidos.calcularComisiones(l_patentes,l_conductores)
        else:
            print("Opcion Invalida")
        opcion=menu()