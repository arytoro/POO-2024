"""Recuperatorio Parcial 2 - Tema 1 - 2024 / Ary Toro"""
from claseEquipo import Equipo

class Nodo:
    __equipo:Equipo
    __siguiente:object

    def __init__(self, equipo):
        self.__equipo= equipo
        self.__siguiente=None

    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente

    def getEquipo(self):
        return self.__equipo

    def getSiguiente(self):
        return self.__siguiente
