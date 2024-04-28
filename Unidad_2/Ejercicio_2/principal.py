"""Ejercicio 1 / Unidad 2 - Ary Toro"""
from claseGestorCajaDeAhorro import GestorDeCajas

if __name__=="__main__":
    cajas= GestorDeCajas()
    cajas.test()
    cajas.mostrar_lista()
    cajas.extraer_lista(1) #Se hará una extraccion en la caja que ocupa la posicion 1 en la lista
    cajas.depositar_lista(0) #Se hará un deposito en la caja de la posicion 0
    cajas.validar_cuil_lista(0) #Se validará el CUIL de la caja de la posicion 0
    CUIL=input("Mensaje de Sistema -> Ingresa el CUIL: ")
    respuesta=cajas.obtenerDatos(CUIL)
    if isinstance(respuesta,str) is True: #Si es str, significa que el CUIL no existe, entonces muestro el mensaje con print
        print(respuesta)
    else: #Sino es str, por descarte es lista, entonces muestro sus datos
        print('°Los datos de la cuenta son: ')
        print('+ Nombre: ',respuesta[0])
        print('+ Apellido: ', respuesta[1])
        print('+ Saldo: ', respuesta[2])

""" Lote de Prueba
567
23-45472019-9
Toro
Cristian
500
910
20-45213500-1
Perez
Pablo
350.8
523
20-45378619-7
Rodriguez
Juan
1500
"""