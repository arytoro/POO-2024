"""Ejercicio 8 / Unidad 3 - Ary Toro"""
from zope.interface import Interface
from zope.interface import implementer
class IDirector(Interface): 
    def modificarBasico(dni,nuevoBasico): 
        pass 
    def modificarPorcentajeporcargo(dni, nuevoPorcentaje): 
        pass 
    def modificarPorcentajeporcategoría(dni, nuevoPorcentaje): 
        pass 
    def modificarImporteExtra(dni, nuevoImporteExtra): 
        pass
