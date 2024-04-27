"""Ejercicio 6 - Unidad 2 / Ary Toro"""

class Cuenta:
    """Clase de cuenta"""
    __ape:str
    __nom:str
    __dni:int
    __tel:int
    __saldo:float
    __cvu:int
    porc_anual=68
    def __init__(self,a,n,d,t,s,c):
        """Metodo constructor de la clase"""
        self.__ape=a
        self.__nom=n
        self.__dni=d
        self.__tel=t
        self.__saldo=s
        self.__cvu=c

    def getApellido(self):
        """Metodo que retorna el apellido del propietario de una cuenta"""
        return self.__ape

    def getNombre(self):
        """Metodo que retorna el nombre del propietario de una cuenta"""
        return self.__nom

    def getDNI(self):
        """Metodo que retorna el dni del propietario de una cuenta"""
        return self.__dni

    def getTelefono(self):
        """Metodo que retorna el telefono del propietario de una cuenta"""
        return self.__tel

    def getSaldo(self):
        """Metodo que retorna el saldo de una cuenta"""
        return self.__saldo

    def getCVU(self):
        """Metodo que retorna el CVU de una cuenta"""
        return self.__cvu

    def getAllDatos(self):
        """Metodo que retorna todos los datos de una cuenta, por defecto lo hace en una tupla"""
        return self.__ape,self.__nom,self.__dni,self.__tel,self.__saldo,self.__cvu

    def actualizarSaldo_Transaccion(self,monto):
        """Metodo que actualiza el saldo con el monto de las transacciones"""
        self.__saldo-=monto
        self.__saldo=round(self.__saldo,2)

    def actualizarSaldo_Incremento(self,porc):
        """Metodo que actualiza el saldo con el incremento diario"""
        self.__saldo+=(porc*self.__saldo)/100 #Regla de 3 simple para calcular el incremento
        self.__saldo=round(self.__saldo,2)

    def mostrarDatos(self):
        """Metodo que muestra los datos de una cuenta"""
        print(f"""
              ------- Datos -------
              °Apellido: {self.__ape}
              °Nombre: {self.__nom}
              °CVU: {self.__cvu}
              °Saldo: ${self.__saldo}""")

        
    @classmethod
    def updatePorcentajeAnual(cls,nuevoP):
        """Metodo de clase que modifica el porcentaje anual"""
        cls.porc_anual=nuevoP

    @classmethod
    def getIncrementoDiario(cls):
        """Metodo que retorna el incremento_diario diario"""
        incremento_diario=round(cls.porc_anual/365,2)#Redondeo a 2 cifras
        return incremento_diario
