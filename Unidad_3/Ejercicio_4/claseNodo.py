"""Ejercicio 4 / Unidad 3 - Ary Toro"""
from clasePublicacion import Publicacion
class Nodo:
    __publicacion: Publicacion
    __siguiente: object

    def __init__(self,publicacion):
        self.__publicacion=publicacion
        self.__siguiente=None

    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente

    def getDato(self):
        return self.__publicacion

    def getSiguiente(self):
        return self.__siguiente
