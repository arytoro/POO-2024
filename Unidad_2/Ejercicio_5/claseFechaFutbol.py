"""Ejercicio 5 / Unidad 2 - Ary Toro"""

class FechaDeFutbol:
    """Clase de fecha"""
    __fechaP:str
    __idEL:int
    __idEV:int
    __cantGolesEL:int
    __cantGolesEV:int

    def __init__(self,fecha,local,visitante,cantGL,cantGV):
        """Metodo constructor de fecha de futbol"""
        self.__fechaP=fecha
        self.__idEL=local
        self.__idEV=visitante
        self.__cantGolesEL=cantGL
        self.__cantGolesEV=cantGV

    def getFecha_Partido(self):
        """Metodo que retorna la fecha del partido"""
        return self.__fechaP

    def getIdLocal_Partido(self):
        """Metodo que retorna el ID del equipo local"""
        return self.__idEL

    def getIdVisitante_Partido(self):
        """Metodo que retorna el ID del equipo visitante"""
        return self.__idEV

    def getGolesLocal_Partido(self):
        """Metodo que retorna los goles que hizo el equipo local"""
        return self.__cantGolesEL

    def getGolesVisitante_Partido(self):
        """Metodo que retorna los goles que hizo el equipo visitante"""
        return self.__cantGolesEV

