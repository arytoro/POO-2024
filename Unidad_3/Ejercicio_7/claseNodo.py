"""Ejercicio 7 / Unidad 3 - Ary Toro"""
from clasePersonal import Personal

class Nodo:
    __personal:Personal
    __siguiente=object

    def __init__(self,personal):
        self.__personal=personal
        self.__siguiente=None

    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente

    def setDato(self,agente):
        self.__personal=agente

    def getDato(self):
        return self.__personal

    def getSiguiente(self):
        return self.__siguiente
