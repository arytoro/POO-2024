"""Ejercicio 5 - Unidad 2 / Ary Toro"""
from claseGestorEquipos import GestorDeEquipo
from claseGestorFechasFutbol import GestorDeFechas

def menu():
    """Funcion de menu de opciones"""
    op=int(input("""
                                 MENÚ DE OPCIONES
          [1] Leer datos de equipos desde archivo csv
          [2] Leer datos de fechas desde archivo csv
          [3] Ingresa nombre del equipo para ver datos
          [4] Actualizar tabla de equipos tras disputar fechas
          [5] Ordenar tabla de posiciones
          [6] Guardar tabla de posiciones ordenada en un csv (tposiciones.csv)
          [7] ADICONAL - Ingresa ID de equipo para eliminar de la liga
          [0] SALIR
          -> """))
    return op

if __name__=='__main__':
    equipos=GestorDeEquipo()
    fechas=GestorDeFechas()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            equipos.test()
            print("Operacion 1 Exitosa!")
        elif opcion==2:
            fechas.test()
            print("Operacion 2 Exitosa!")
        elif opcion==3:
            #idsYnombres=equipos.getListaEquipos_IDyNom()
            nombreOP3=input("Ingresa el nombre del equipo que buscas: ")
            idEquipo=equipos.getIdPorNombre(nombreOP3)
            if idEquipo!=-1:
                fechas.mostrarDatosEquipo(idEquipo,nombreOP3)
            else:
                print("El equipo no existe")

        elif opcion==4:
            resultados=fechas.getResultados()
            equipos.actualizar(resultados)
            equipos.mostrarTablaEquipos()

        elif opcion==5:
            equipos.ordenar()
            equipos.mostrarTablaEquipos()

        elif opcion==6:
            equipos.guardarCSV()

        elif opcion==7:
            nombreOP7=int(input("Ingresa la ID del equipo a borrar: "))
            equipos.eliminarEquipo(nombreOP7)
        else:
            print('Opcion Invalida')
        opcion=menu()
    