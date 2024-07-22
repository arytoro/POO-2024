"""Recuperatorio Parcial 2 - Tema 1 - 2024 / Ary Toro"""
from abc import ABC,abstractmethod

class Equipo(ABC):
    __marca:str
    __modelo:str
    __anioF:int
    __tipoC:str
    __potencia:float
    __capacidad:int
    __tarifaAlq:float
    __diasAlq:int

    def __init__(self,mar,mod,anio,tipo,pote,cap,tar,dias):
        self.__marca=mar
        self.__modelo=mod
        self.__anioF=anio
        self.__tipoC=tipo
        self.__potencia=pote
        self.__capacidad=cap
        self.__tarifaAlq=tar
        self.__diasAlq=dias

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getAnioFab(self):
        return self.__anioF

    def getTipoComb(self):
        return self.__tipoC

    def getPotencia(self):
        return self.__potencia

    def getCapacidad(self):
        return self.__capacidad

    def getTarifaAlquilerDiario(self):
        return self.__tarifaAlq

    def getDiasAlquiler(self):
        return self.__diasAlq

    @abstractmethod
    def getTarifaAlquilerTotal(self):
        pass
