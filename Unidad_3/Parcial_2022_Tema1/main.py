from claseListaVehiculos import Lista
from claseVehiculoCarga import VehiculoCarga
from claseVehiculoPasajeros import VehiculoPasajero
def menu():
    op=None
    try:
        op=int(input("""
                        Menu de Opciones
        [1] Agregar Vehiculo a la coleccion
        [2] Mostrar datos de Vehiculos de Pasajeros con mas de 6 asientos
        [3] Mostrar cantidad de Vehiculos de Carga de una marca
        [4] Listar datos de todos los vehiculos
        [0] Salir
        -> """))
    except ValueError:
        pass
    return op

if __name__=='__main__':
    GV=Lista()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            try:
                tipo=int(input("De que tipo?\n  [1] De Pasajeros\n  [2] De Carga\n  [0] Cancelar\n   -> "))
                while tipo not in (1,2,0):
                    tipo=int(input("Tipo Invalido! Las opciones son:\n  [1] De Pasajeros\n  [2] De Carga\n   [0] Cancelar\n   -> "))
                if tipo!=0:
                    marca=input("Ingresa la Marca: ")
                    modelo=input("Modelo: ")
                    pate=input("Patente: ")
                    iba=float(input("IBA: "))
                    km=float(input("Cantidad de KM a recorrer: "))
                    if tipo==1:
                        ca=int(input("Cantidad de Asientos: "))
                        nuevoVehiculo=VehiculoPasajero(ca,Marca=marca,Modelo=modelo,Patente=pate,ImpA=iba,CantKM=km)
                    else:
                        pc=float(int(input("Peso de Carga: ")))
                        nuevoVehiculo=VehiculoCarga(pc,Marca=marca,Modelo=modelo,Patente=pate,ImpA=iba,CantKM=km)
                    GV.agregarVehiculo(nuevoVehiculo)
                else:
                    print("...Cancelando operacion de carga")
            except ValueError:
                print('Error. Se esperaba un numero')
        elif opcion==2:
            GV.mostrarDatosVehiculosPasajeros()
        elif opcion==3:
            xmarca=input("Ingresa la marca: ").strip().lower()
            GV.mostrarCantidadVehiculosCarga(xmarca)
        elif opcion==4:
            GV.listarVehiculos()
        else:
            print("Opcion Invalida!")
        opcion=menu()

"""Lote De Prueba (ejecutar y pegar todo lo de abajo)
1
1
Toyota
Corolla
ABC 123
120000
230
8
1
1
Ford
Focus
DEF 456
230000
300
4
1
2
Chevrolet
Cruze
GHI 789
420000
850
600
1
1
Volkswagen
Golf
JKL 012
290000
460
7
1
2
Nissan
Civic
MNO 345
500000
1450
400
1
2
Nissan
Sentra
PQR 678
410000
670
780
1
1
BMW
Serie 3
STU 901
600000
1540
2
1
2
Mercedes-Benz
Clase C
VWX 234
680000
829
620
"""

