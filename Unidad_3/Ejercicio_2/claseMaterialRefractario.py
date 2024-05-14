"""Ejercicio 2 / Unidad 3 - Ary Toro"""
class MaterialRefractario:
    __material:int
    __caracteristicas:str
    __cantUsada:float
    __costoAdicional:float

    def __init__(self,material,carac,cant,costo):
        self.__material=material
        self.__caracteristicas=carac
        self.__cantUsada=cant
        self.__costoAdicional=costo

    def getMaterial(self):
        return self.__material

    def getCaracteristicas(self):
        return self.__caracteristicas

    def getCantUsada(self):
        return self.__cantUsada

    def getCostoAdicional(self):
        return self.__costoAdicional
