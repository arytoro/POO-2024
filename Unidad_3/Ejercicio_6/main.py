"""Ejercicio 6 / Unidad 3 - Ary Toro"""
from claseObjectEncoder import ObjectEncoder
from claseIInterfaz import IInterfaz
from claseListaCalefactores import Lista

def interfaz(manejarInterfaz:IInterfaz,accion,calefactor=None,pos=None):
    if accion==1:
        manejarInterfaz.insertarElemento(calefactor,pos)
    elif accion==2:
        manejarInterfaz.agregarElemento(calefactor)
    else:
        manejarInterfaz.mostrarElemento()

def menu():
    op=None
    try:
        op=int(input("""
                        Menú de Opciones
    [1] Insertar un calefactor en una posicion determinada de la lista
    [2] Agregar un calefactor al final de la lista
    [3] Mostrar el tipo de calefactor de una posicion
    [4] Mostrar datos de calefactor a gas de menor precio
    [5] Ingresa una marca de calefactor electrico para listar dichos calefactores
    [6] Mostrar datos de calefactores en promocion
    [7] Guardar cambios en calefactores.json
    [8] ADICIONAL. Listar calefactores con indices
    [0] SALIR
     -> """))
    except ValueError:
        pass
    return op


if __name__=='__main__':
    jsonF=ObjectEncoder()
    GC=Lista()
    diccionario=jsonF.leerJSONArchivo('calefactores.json')
    GC=jsonF.decodificarDiccionario(diccionario)
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            try:
                indice=int(input("Indica la posicion a insertar: "))
                nuevoCalefactor=GC.crearCalefactor()
                if nuevoCalefactor is not None: #Si es None es porque se cancelo la operacion de carga
                    interfaz(IInterfaz(GC),opcion,nuevoCalefactor,indice)
            except ValueError:
                print("ERROR. Se esperaba un numero")

        elif opcion==2:
            nuevoCalefactor=GC.crearCalefactor()
            if nuevoCalefactor is not None: #Si es None es porque se cancelo la operacion de carga
                interfaz(IInterfaz(GC),opcion,nuevoCalefactor)
        elif opcion==3:
            interfaz(IInterfaz(GC),opcion)
        elif opcion==4:
            GC.mostrarDatosCalefactorGas_MenorPrecio()
        elif opcion==5:
            GC.mostrarDatosCalefactorElectrico_PorMarca()
        elif opcion==6:
            GC.mostrarDatosCalefactores_EnPromocion()
        elif opcion==7:
            d= GC.toJSON()
            jsonF.guardarJSONArchivo(d,'calefactores.json')
            print("Cambios guardados exitosamente!")
        elif opcion==8:
            GC.listarCalefactores()
        else:
            print("Opcion Invalida!")
        opcion=menu()

"""
0
1
Ginova
082-462
China
650
contado
si
5000
1
0
2
Espagueti
123-456
Rusia
980
cuotas
6
no
Aksdj-9302
3000
1
1
2
Albondiga
821-561
Peru
1300
contado
no
skieg-1275
2500
1
3
1
Ginova
782-dk3
Uruguay
1600
contado
si
4000
1
1
1
Ropero
627-35g
Surinam
4900
contado
no
1600
"""