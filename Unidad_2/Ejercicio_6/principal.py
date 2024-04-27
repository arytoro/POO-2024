"""Ejercicio 6 - Unidad 2 / Ary Toro"""
from claseGestorCuentas import GestorCuentas
from claseGestorTransacciones import GestorTransacciones

def menu():
    """Funcion menu de opciones"""
    op=int(input("""
                                Menú de opciones
        [1] Ingresa DNI del cliente para ver datos(datos actualizados con csv de transacciones)
        [2] Modificar el porcentaje anual de rendimiento
        [3] Actualizar el saldo de los clientes con el incremento diario
        [4] Ingresa CVU para ver saldo pre y post transacciones
        [5] Guardar CSV con todas las actualizaciones realizadas (updateCuentas.csv)
        [6] ADICIONAL - Ingresa numero de transaccion para eliminarla
        [7] ADICIONAL - Ver cuentas existentes y su estado
        [0] SALIR
        -> """))
    return op

if __name__=='__main__':
    cuentas=GestorCuentas()
    transacciones=GestorTransacciones()
    cuentas.test()
    transacciones.test()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            dni_op1=int(input("Ingresa el DNI del cliente: "))
            cvu_op1=cuentas.getCVUporDNI(dni_op1)
            if cvu_op1!=-1:
                monto_transacciones_op1=transacciones.getTransaccionesPorCVU(cvu_op1)#Aqui tengo el monto total de todas sus transacciones
                cuentas.actualizarPostTransacciones(cvu_op1,monto_transacciones_op1)
                cuentas.mostrarDatosParaCVU(cvu_op1)
            else:
                print("No existe el DNI ingresado")
        elif opcion==2:
            nuevo_porc=float(input("Ingresa el nuevo porcentaje anual: "))
            cuentas.actualizarPorcentajeAnual(nuevo_porc)
        elif opcion==3:
            pi_diario=cuentas.getPI_Diario()#pi_diario tiene el porc de incremento diario
            #print(pi_diario)
            cuentas.actualizarPostIncremento(pi_diario)
        elif opcion==4:
            cvu_op4=int(input("Ingresa el CVU de la cuenta: "))
            pre_transaccion=cuentas.getSaldoPorCVU(cvu_op4)#Esta variable puede tener el monto si existe el CVU, o un str si no existe el CVU
            if isinstance(pre_transaccion,float):#Si es float significa que tiene el monto, por lo tanto existe el CVU
                print("Su saldo pre-transacciones es: ",pre_transaccion)
                monto_transacciones_op4=transacciones.getTransaccionesPorCVU(cvu_op4)#Aqui tengo el monto total de todas sus transacciones
                cuentas.actualizarPostTransacciones(cvu_op4,monto_transacciones_op4)
                print("Su saldo post-transacciones es: ",cuentas.getSaldoPorCVU(cvu_op4))
            else:
                print(pre_transaccion)#Sino es float, por descarte es str, por lo tanto lo muestro con print
        elif opcion==5:
            cuentas.guardarCSV()
        elif opcion==6:
            numt_op6=int(input("Ingresa el numero de la transaccion a eliminar: "))
            transacciones.eliminarTransaccion(numt_op6)
        elif opcion==7:
            cuentas.verEstadoCuentas()
        else:
            print("Opcion invalida!")
        opcion=menu()