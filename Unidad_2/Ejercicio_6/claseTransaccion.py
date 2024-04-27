"""Ejercicio 6 - Unidad 2 / Ary Toro"""
class Transaccion:
    """Clase de transacciones"""
    __cvu:int
    __numt:int
    __imp:float
    __tipo:str

    def __init__(self,c,n,i,t):
        """Metodo constructor de la clase"""
        self.__cvu=c
        self.__numt=n
        self.__imp=i
        self.__tipo=t

    def getCVU(self):
        """Metodo que devuelve el CVU de la transaccion"""
        return self.__cvu

    def getImporte(self):
        """Metodo que retora el importe de la transaccion"""
        return self.__imp

    def getNumero(self):
        """Metodo que retorna el numero de transaccion"""
        return self.__numt

    def __del__(self):
        """Metodo destructor"""
        print("Se elimino una transaccion de la cuenta con CVU: ",self.__cvu)
