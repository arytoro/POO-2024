"""Ejercicio 5 / Unidad 3 - Ary Toro"""
#Se debe instalar la libreria zope con: pip install zope.interface
from zope.interface import Interface
from zope.interface import implementer

class IInterfaz(Interface):
    def insertarElemento(elemento,pos):
        pass
    def agregarElemento(elemento):
        pass
    def mostrarElemento():
        pass
