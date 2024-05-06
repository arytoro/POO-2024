from claseGestorDeClientes import GestorDeClientes
from claseGestorDeMovimientos import GestorDeMovimientos

def menu():
    op:int
    op=int(input("""
                                    Menú de Opciones
                [1] Ingresa DNI de cliente para actualizar saldo con operaciones
                [2] Ingresa DNI del cliente para mostrar nombre y apellido si no tuvo movimientos
                [3] Ordenar movimientos por numero de cuentas
                [0] Salir
                -> """))
    return op

if __name__=='__main__':
    opcion:int
    GC= GestorDeClientes()
    GM= GestorDeMovimientos()
    GC.test()
    GM.test()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            GC.actualizarSaldo_conOperaciones(GM)
        elif opcion==2:
            GC.mostrarDatos_siNoTieneMovimientos(GM)
        elif opcion==3:
            GM.ordenarMovimientos()
            GM.listarMovimientos()
        else:
            print("Opcion invalida!")
        opcion=menu()
