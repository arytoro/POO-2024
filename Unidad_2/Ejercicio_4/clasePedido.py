"""Ejercicio 4 / Unidad 2 - Ary Toro"""

class Pedido:
    """Clase de Pedidos"""
    __patente:str
    __id:int
    __comida:str
    __tiempoE:int
    __tiempoR:int
    __precio:float

    def __init__(self,pat,i,c,te,p,tr=0):
        """Metodo constructor de Moto"""
        self.__patente=pat
        self.__id=i
        self.__comida=c
        self.__tiempoE=te
        self.__tiempoR=tr
        self.__precio=p

    def getPatente(self):
        """Metodo que retorna la patente"""
        return self.__patente

    def getID(self):
        """Metodo que retorna el ID"""
        return self.__id

    def getComida(self):
        """Metodo que retorna la comida"""
        return self.__comida

    def getTiempoEstimado(self):
        """Metodo que retorna el tiempo estimado"""
        return self.__tiempoE

    def getPrecio(self):
        """Metodo que retorna el precio del pedido"""
        return self.__precio

    def getTiempoReal(self):
        """Metodo que retorna el tiempo real"""
        return self.__tiempoR

    def setTiempoReal(self,entrega):
        """Metodo que retorna el tiempo real"""
        self.__tiempoR=entrega
        print('...Tiempo real de entrega modificado!')

    def __lt__(self,otro):
        """Sobrecarga del operador < para el ordenamiento"""
        #Lo usa internamente la funcion sorted
        return self.__patente < otro.getPatente()
