"""Ejercicio 4 / Unidad 2 - Ary Toro"""

class Moto:
    """Clase de Motos"""
    __patente:str
    __marca:str
    __conductor:str
    __kilometraje:int

    def __init__(self,p,m,c,k):
        """Metodo constructor de Moto"""
        self.__patente=p
        self.__marca=m
        self.__conductor=c
        self.__kilometraje=k

    def getPatente(self):
        """Metodo que retorna la patente"""
        return self.__patente

    def getMarca(self):
        """Metodo que retorna la marca"""
        return self.__marca

    def getConductor(self):
        """Metodo que retorna el conductor"""
        return self.__conductor

    def getKilometraje(self):
        """Metodo que retorna su kilometraje"""
        return self.__kilometraje
