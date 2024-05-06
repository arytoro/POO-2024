
class Cliente:
    __nombre:str
    __apellido:str
    __dni:int
    __numeroCuenta:int
    __saldoAnterior:float

    def __init__(self,nom,ape,dni,num,sal):
        self.__nombre=nom
        self.__apellido=ape
        self.__dni=dni
        self.__numeroCuenta=num
        self.__saldoAnterior=sal

    def getDNI(self):
        return self.__dni

    def getNumCuenta(self):
        return self.__numeroCuenta

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getSaldo(self):
        return self.__saldoAnterior

    def __lt__(self,otro):
        return self.__numeroCuenta < otro.getNumCuenta()

    def __str__(self):
        return f"{self.__apellido, self.__nombre, self.__numeroCuenta}"