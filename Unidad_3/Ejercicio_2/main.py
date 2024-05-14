"""Ejercicio 2 / Unidad 3 - Ary Toro"""
from gestorLadrillos import GestorDeLadrillos
from gestorMateriales import GestorDeMateriales

def menu():
    op=None
    try:
        op=int(input("""
                                Menú de Opciones 
                [1] Ingresa ID de ladrillo para conocer costo y característica del material
                [2] Listar costo total de fabricacion de todos los ladrillos
                [3] Mostar detalles de ladrillos
                [0] SALIR
                -> """))
    except ValueError:
        pass
    return op

if __name__=='__main__':
    GL=GestorDeLadrillos()
    GM=GestorDeMateriales()
    GL.cargarLadrillos()
    GM.cargarMateriales()
    GL.asignarMateriales(GM)
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            try:
                idOp1=int(input("Ingresa el ID: "))
                GL.mostrarDatosMateriales(idOp1)
            except ValueError:
                print("Entrada invalida. Se esperaba un entero")
        elif opcion==2:
            GL.mostrarCostosTotalDeFabricacion()
        elif opcion==3:
            GL.mostrarDetallesLadrillos()
        else:
            print("Opcion Invalida!")
        opcion=menu()