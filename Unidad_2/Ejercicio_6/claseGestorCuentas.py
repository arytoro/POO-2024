"""Ejercicio 6 - Unidad 2 / Ary Toro"""
import numpy as np
import csv
from claseCuenta import Cuenta
class GestorCuentas:
    """Clase del gestor de cuentas"""
    __cantidad:int
    __dimension:int
    __incremento:int
    __cuentas: np.ndarray
    def __init__(self):
        """Metodo constructor del gestor de ventas"""
        self.__cantidad=0
        self.__dimension=0
        self.__incremento=5
        self.__cuentas=np.empty(self.__dimension,dtype=Cuenta)

    def agregarCuenta(self,unacuenta):
        """Metodo para agregar una cuenta al arreglo de cuentas"""
        if self.__cantidad == self.__dimension:
            print("Se solicito espacio")
            self.__dimension += self.__incremento
            self.__cuentas.resize(self.__dimension)
        self.__cuentas[self.__cantidad]=unacuenta
        self.__cantidad+=1

    def test(self):
        """Metodo para leer cuentas desde archivo"""
        archivo= open('cuentasBilletera.csv')
        reader= csv.reader(archivo,delimiter=';')
        band=True
        for fila in reader:
            if band:
                band=not band
            else:
                self.agregarCuenta(Cuenta(fila[0],fila[1],int(fila[2]),int(fila[3]),float(fila[4]),int(fila[5])))
        #self.__cuentas.resize(self.__cantidad) #Saca las posiciones que quedaron vacias
        archivo.close()

    def getCVUporDNI(self,dni):
        """Metodo que retorna el CVU de una cuenta a partir del DNI del propietario"""
        long= self.__cantidad
        i=0
        band=False
        while band is False and i<long:
            if dni==self.__cuentas[i].getDNI():
                cvu=self.__cuentas[i].getCVU()
                band=True
            else:
                i+=1
        if band is False:
            return -1
        else:
            return cvu

    def actualizarPostTransacciones(self,cvu,monto):
        """Actualiza el saldo de la cuenta despues de realizarse las transacciones"""
        i=0
        long=self.__cantidad
        band=False
        while band is False and i<long:
            if cvu==self.__cuentas[i].getCVU():
                self.__cuentas[i].actualizarSaldo_Transaccion(monto)
                band=True
            else:
                i+=1
        print(f"Se actualizo el saldo de la cuenta de CVU:{self.__cuentas[i].getCVU()} con sus transacciones!")

    def mostrarDatosParaCVU(self,cvu):
        """Muestra los datos de la cuenta con el cvu ingresado"""
        i=0
        long=self.__cantidad
        band=False
        while band is False and i<long:
            if cvu==self.__cuentas[i].getCVU():
                self.__cuentas[i].mostrarDatos()
                band=True
            else:
                i+=1

    def actualizarPorcentajeAnual(self,nuevoP):
        """Metodo que llama al metodo de clase updatePorcentajeAnual para actualizar el porcentaje anual"""
        self.__cuentas[0].updatePorcentajeAnual(nuevoP)
        #El 0 entre corchetes podria ser otro indice, es indiferente, ya que si se modifica
        # un atributo de clase para una instancia, tambien se modifica para todas las demas
        # Es recomendable hacerlo con 0 ya que se supone existe almenos un objeto en el manejador
    def getPI_Diario(self):
        """Metodo que llama al metodo de clase getIncrementoDiario para retornar dicho valor"""
        return self.__cuentas[0].getIncrementoDiario()

    def actualizarPostIncremento(self,porcentaje):
        """Metodo que actualiza el saldo de todas las cuentas con el incremento diario"""
        for i in range(self.__cantidad):
            self.__cuentas[i].actualizarSaldo_Incremento(porcentaje)
            self.__cuentas[i].mostrarDatos()
        print("Se actualizaron los saldos de las cuentas! Se recuerda que el incremento diario es %",porcentaje)

    def getSaldoPorCVU(self,cvu):
        """Metodo que retorna el saldo actual de una cuenta con dicho CVU"""
        long= self.__cantidad
        i=0
        band=False
        while band is False and i<long:
            if cvu==self.__cuentas[i].getCVU():
                saldo=self.__cuentas[i].getSaldo()
                band=True
            else:
                i+=1
        if band is False:
            return "No existe el CVU"
        else:
            return saldo

    def getLista_DatosCuentas(self):
        """Metodo que retorna una lista con los datos de las cuentas a actualizar"""
        lista=[]
        print(self.__cuentas.size)
        for i in range(self.__cantidad):
            lista.append(self.__cuentas[i].getAllDatos())
        return lista #Es una lista de tuplas, cada tupla contiene los datos de una cuenta

    def guardarCSV(self):
        """Metodo que guarda los datos actuales de las cuentas en un archivo csv"""
        cuentas_actualizadas=self.getLista_DatosCuentas()
        #print(cuentas_actualizadas) #Podes descomentar esta linea para ver la lista de tuplas
        archivo=open("updateCuentas.csv",mode='w',newline='')
        writer=csv.writer(archivo,delimiter=";")
        for fila in cuentas_actualizadas:
            writer.writerow(fila)
        archivo.close()
        print("Se guardaron los datos exitosamente!")

    def verEstadoCuentas(self):
        """Metodo que muestra el estado de todos los atributos de una cuenta"""
        #No lo pide la consigna, lo inclui para hacer un seguimiento
        cuentas=self.getLista_DatosCuentas()
        print("     CVU         DNI         TELEFONO          SALDO        APELLIDO Y NOMBRE")
        for unacuenta in cuentas:
            cvu=unacuenta[5]
            dni=unacuenta[2]
            tel=unacuenta[3]
            saldo=unacuenta[4]
            ayn=unacuenta[0]+" "+unacuenta[1] #Uno dos strings con un espacio de por medio
            print(f"    {cvu}   {dni}      {tel}        {saldo}        {ayn}")
