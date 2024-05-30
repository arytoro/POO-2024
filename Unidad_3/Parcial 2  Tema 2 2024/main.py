from claseGestorVehiculos import GestorVehiculos,Autobus,Van

def menu():
    op=None
    try:
        op=int(input("""
                                Menu de Opciones
            [1] Agregar vehiculo a la coleccion
            [2] Mostrar tipo de vehiculo almacenado en una posicion
            [3] Mostrar cantidad de vehiculos de cada tipo
            [4] Listar datos de todos los vehiculos
            [0] SALIR
            -> """))
    except ValueError:
        pass
    return op

if __name__=='__main__':
    GV=GestorVehiculos()
    GV.cargarArchivosCSV()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            try:
                tipoVehi=int(input("De que tipo?\n   [1] Autobus\n   [2] Van\n   [0] Cancelar\n   -> "))
                while tipoVehi not in (1,2,0):
                    tipoVehi=int(input("Opcion Invalida! Las opciones son:\n   [1] Autobus\n   [2] Van\n   [0] Cancelar\n   -> "))
                if tipoVehi!=0:
                    mar=input("Ingresa la marca: ")
                    mod=input("Modelo: ")
                    anio=int(input("Anio de Fabricacion: "))
                    cap=int(input("Capacidad de Pasajeros: "))
                    numP=int(input("Numero de Plazas: "))
                    distR=float(input("Distancia Recorrida: "))
                    tarB=float(input("Tarifa Base: "))

                    if tipoVehi==1:
                        tipoS=input("Tipo de Servicio: ").strip().lower()
                        turnoS=input("Turno del Servicio: ").strip().lower()
                        nuevoVehiculo=Autobus(mar,mod,anio,cap,numP,distR,tarB,tipoS,turnoS)
                    else:
                        tipoC=input("Tipo de Carroceria: ").strip().lower()
                        nuevoVehiculo=Van(mar,mod,anio,cap,numP,distR,tarB,tipoC)
                    GV.agregarVehiculo(nuevoVehiculo)
                else:
                    print("....Cancelando operacion de carga")
            except ValueError:
                print("ERROR. Se esperaba un numero")
        elif opcion==2:
            try:
                posicion=int(input("Ingresa la posicion: "))
                GV.mostrarTipoVehiculo_PorIndice(posicion)
            except ValueError:
                print("ERROR. Se esperaba un numero")
            except IndexError:
                print("ERROR. El indice ingresado no corresponde a un elemento de la lista")
        elif opcion==3:
            GV.mostrarCantidadVehiculos_PorTipos()
        elif opcion==4:
            GV.listarDatosVehiculos()
        else:
            print("Opcion Invalida!")
        opcion=menu()
