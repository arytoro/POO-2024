"""Ejercicio 1 / Unidad 3 - Ary Toro"""
from claseGestorEdificios import GestorDeEdificios

def menu():
    op=None
    try:
        op=int(input("""
                                Menú De Opciones
                [1] Ingresa nombre de edificio para conocer propietarios de sus departamentos
                [2] Conocer superficie total cubierta de un edificio
                [3] Conocer superficie total de departamento/s de un propietario
                [4] Ingresa numero de piso para conocer deptos con mas de un baño y 3 dormitorios
                [0] SALIR
                -> """))
    except ValueError:
        pass #No quiero mostrar un print, para eso esta la "validacion" de opciones en el menu
    return op

if __name__=="__main__":
    GE=GestorDeEdificios()
    GE.cargarEdificios()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            try:
                nombreOp1=input("Ingresa el nombre del edificio: ")
                GE.mostrarPropietarios(nombreOp1)
            except AssertionError:
                print("Error. No existe un edificio con ese nombre")

        elif opcion==2:
            try:
                idOp2=int(input("Ingresa la ID del edificio: "))
                GE.mostrarSuperficieTotalEdificio(idOp2)
            except ValueError:
                print("Error. Se esperaba un numero entero")
            except AssertionError:
                print("Error. No existe un edificio con esa ID")

        elif opcion==3:
            try:
                nombreOp3=input("Ingresa el nombre del propietario: ")
                GE.mostrarSuperficieTotalDepartamento(nombreOp3)
            except AssertionError:
                print("Error. No existe un propietario con ese nombre")

        elif opcion==4:
            try:
                pisoOp4=int(input("Ingresa el numero de piso: "))
                GE.mostrarDepartamentosConCondiciones(pisoOp4)
            except ValueError:
                print("Error. Se esperaba un numero entero")
            except AssertionError:
                print("Error. No existe ese numero de piso para ningun departamento")
        else:
            print("Opcion Invalida!")
        opcion=menu()
