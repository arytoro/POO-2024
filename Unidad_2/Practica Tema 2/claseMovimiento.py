

class Movimiento:
    __numeroCuenta:int
    __fecha:str
    __descripcion:str
    __tipo:str
    __importe:float

    def __init__(self,num,fecha,desc,tipo,imp):
        self.__numeroCuenta=num
        self.__fecha=fecha
        self.__descripcion=desc
        self.__tipo=tipo
        self.__importe=imp

    def getNumCuenta(self):
        return self.__numeroCuenta

    def getFecha(self):
        return self.__fecha

    def getDescripcion(self):
        return self.__descripcion

    def getImporte(self):
        return self.__importe

    def getTipo(self):
        return self.__tipo

    def __lt__(self,otro):
        return self.__numeroCuenta < otro.getNumCuenta()

    def __str__(self):
        return f"{self.__numeroCuenta, self.__tipo}"
