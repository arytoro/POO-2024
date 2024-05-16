"""Ejercicio 3 / Unidad 3 - Ary Toro"""
from gestorEmpleados import GestorEmpleados
from gestorProgramas import GestorDeProgramas
from gestorMatriculas import GestorMatriculas
def menu():
    op=None
    try:
        op=int(input("""
                                    Menú de Opciones
        [1] Ingrese ID de empleado para conocer duracion de cursos en que esta matriculado
        [2] Ingresa nombre de programa para conocer empleados matriculados en el mismo
        [3] Listar empleados que no estan matriculados a programas
        [4] Adicional. Borrar matricula por indice
        [0] Salir
        -> """))
    except ValueError:
        pass
    return op

if __name__=='__main__':
    GE=GestorEmpleados()
    GP=GestorDeProgramas()
    GM=GestorMatriculas()
    GE.cargarEmpleados()
    GP.cargarProgramas()
    GE.asignarMatriculaciones(GP,GM) #Las direcciones de memorias que quedaron
    print("----Lista de Matriculas----")
    GM.listarMatriculas()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            try:
                idOp1=int(input("Ingresa su ID: "))
                GE.mostrarDuracionDeProgramasEmpleado(idOp1)
            except ValueError:
                print("Error. Se esperaba un numero entero")
            except AssertionError:
                print("Error. El ID ingresado no pertence a un empleado")
        elif opcion==2:
            try:
                nomOp2=input("Ingresa su nombre: ")
                GP.mostrarEmpleadosDePrograma(nomOp2)
            except AssertionError:
                print("Error. El nombre ingresado no pertence a un programa")
        elif opcion==3:
            try:
                GE.mostrarEmpleadosSinMatriculas()
            except ValueError:
                print("Todos los empleados se encuentran matriculados a programas")
        elif opcion==4:
            GM.borrarMatriculaPorIndice(2) #Le puse 2 para probar si
            GM.listarDireccionesMatriculas()
            GM.listarMatriculas()
        else:
            print("Opcion Invalida!")
        opcion=menu()
