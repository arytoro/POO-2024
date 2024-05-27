"""Ejercicio 7 / Unidad 3 - Ary Toro"""
import abc
from abc import ABC
class Personal(ABC):
    __cuil:str
    __apellido:str
    __nombre:str
    __sueldoBasico:float
    __antiguedad:int

    def __init__(self,**kwargs):
        self.__cuil=kwargs['Cuil']
        self.__apellido=kwargs['Ape']
        self.__nombre=kwargs['Nom']
        self.__sueldoBasico=kwargs['SueldoB']
        self.__antiguedad=kwargs['Antig']

    def getCuil(self):
        return self.__cuil

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getSueldoBasico(self):
        return self.__sueldoBasico

    def getAntiguedad(self):
        return self.__antiguedad

    def setSueldoBasico(self,nuevoBasico):
        self.__sueldoBasico=nuevoBasico

    @abc.abstractmethod
    def getSueldoTotal(self):
        pass
    @abc.abstractmethod
    def toJSON(self):
        pass
