"""Recuperatorio Parcial 2 - Tema 1 - 2024 / Ary Toro"""
from claseLista import Lista

def menu():
    op=None
    try:
        op=int(input("""
                     Menu de Opciones
        [1] Ingresa un indice para conocer el tipo del equipo
        [2] Ingresa anio para conocer cantidad herramientas electricas fabricadas en el mismo
        [3] Ingresa capacidad para conocer cantidad de maquinarias pesadas cuya capacidad es igual o inferior
        [4] Listar datos de todos los equipos
        [0] SALIR
        -> """))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    GE=Lista()
    GE.cargarEquipos()
    GE.listarCantidad()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            try:
                pos=int(input("Ingresa el indice: "))
                GE.mostrar_tipo(pos)
            except ValueError:
                print("Error. El indice debe ser un numero entero")
            except IndexError:
                print("Indice fuera de rango")
        elif opcion==2:
            try:
                anio=int(input("Ingresa el anio: "))
                GE.mostrar_cantidad_HE_anio(anio)
            except ValueError:
                print("Error. El anio debe ser un numero entero")
        elif opcion==3:
            try:
                cap=float(input("Ingresa la capacidad: "))
                GE.mostrar_cantidad_MP_capacidad(cap)
            except ValueError:
                print("Error. La capacidad debe ser expresada numericamente")
        elif opcion==4:
            GE.listar_datos_equipos()
        else:
            print("Opcion Invalida!")
        opcion=menu()
