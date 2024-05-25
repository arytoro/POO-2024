""""Ejercicio 6 / Unidad 3 - Ary Toro"""
import json
from pathlib import Path
import abc
from abc import ABC
class Calefactor(ABC):
    __marca:str
    __modelo:str
    __paisFabrica:str
    __precio:float
    __fpago:str
    __cantCuotas:int
    __promocion:str
    
    def __init__(self,marca,modelo,paisf,precio,fpago,cantcuotas,promo):
        self.__marca=marca
        self.__modelo=modelo
        self.__paisFabrica=paisf
        self.__precio=precio
        self.__fpago=fpago
        self.__cantCuotas=cantcuotas
        self.__promocion=promo

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getPaisFabrica(self):
        return self.__paisFabrica

    def getPrecio(self):
        return self.__precio

    def getFormaPago(self):
        return self.__fpago

    def getCantCuotas(self):
        return self.__cantCuotas

    def getPromocion(self):
        return self.__promocion

    @abc.abstractmethod
    def toJSON(self):
        pass

    @abc.abstractmethod
    def getImporteVenta(self):
        pass
