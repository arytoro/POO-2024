"""Ejercicio 4 / Unidad 3 - Ary Toro"""
import abc
from abc import ABC

class Publicacion(ABC):
    __titulo:str
    __categoria:str
    __precioBase:float

    def __init__(self,tit,cate,precioB):
        self.__titulo=tit
        self.__categoria=cate
        self.__precioBase=precioB

    def getTitulo(self):
        return self.__titulo

    def getCategoria(self):
        return self.__categoria

    def getPrecioBase(self):
        return self.__precioBase

    @abc.abstractmethod
    def getImporteVenta(self):
        pass
