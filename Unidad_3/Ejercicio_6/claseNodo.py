"""Ejercicio 6 / Unidad 3 - Ary Toro"""
from claseCalefactor import Calefactor

class Nodo:
    __calefactor:Calefactor
    __siguiente=object

    def __init__(self,calefactor):
        self.__calefactor=calefactor
        self.__siguiente=None

    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente

    def getDato(self):
        return self.__calefactor

    def getSiguiente(self):
        return self.__siguiente
