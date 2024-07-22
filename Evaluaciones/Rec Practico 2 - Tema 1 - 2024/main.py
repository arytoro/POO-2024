"""Recuperatio Practico 2 - Tema 1 - 2024 / Ary Toro"""
from gestorMamas import GestorDeMamas
from gestorNacimientos import GestorDeNacimientos

def menu():
    op=None
    try:
        op=int(input("""
                                Menu de Opciones
                [1] Ingresa el DNI de una madre para obtener su informacion
                [2] Mostrar informacion de madres que tuvieron multiples partos
                [0] Salir
                -> """))
    except ValueError:
        pass
    return op

if __name__=='__main__':
    GM=GestorDeMamas()
    GN=GestorDeNacimientos()
    GM.cargarMadres()
    GN.cargarNacimientos()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            try:
                dni=int(input("Ingresa el DNI: "))
                GM.mostrar_datos_mama(dni,GN)
            except ValueError:
                print("ERROR! El DNI solo debe contener numeros")
            except AssertionError:
                print("ERROR. El DNI ingresado no pertenece a una madre")
        elif opcion==2:
            GN.detectar_partos_multiples(GM)
        else:
            print("Opcion Invalida!")
        opcion=menu()