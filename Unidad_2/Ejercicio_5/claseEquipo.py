"""Ejercicio 5 / Unidad 2 - Ary Toro"""

class Equipo:
    """Clase de equipo"""
    __id_e:int
    __nombre_e:str
    __golesF:int
    __golesC:int
    __puntos:int
    __difGol:int

    def __init__(self,ide,nom,gf,gc,pun):
        """Metodo constructor de equipo"""
        self.__id_e=ide
        self.__nombre_e=nom
        self.__golesF=gf
        self.__golesC=gc
        self.__puntos=pun
        self.__difGol=gf-gc

    def getID_Equipo(self):
        """Metodo que retorna la ID del equipo"""
        return self.__id_e

    def getNombre_Equipo(self):
        """Metodo que retorna el nombre del equipo"""
        return self.__nombre_e

    def getGolesF_Equipo(self):
        """Metodo que retorna los goles a favor del equipo"""
        return self.__golesF

    def getGolesC_Equipo(self):
        """Metodo que retorna los goles en contra del equipo"""
        return self.__golesC

    def getPuntos_Equipo(self):
        """Metodo que retorna los puntos del equipo"""
        return self.__puntos

    def getDifGoles_Equipo(self):
        """Metodo que retorna los goles a favor del equipo"""
        return self.__difGol

    def updatePostFecha(self,golesf,golesc):
        """Metodo que actualiza el estado de un equipo tras disputar las fechas"""
        diferencia_gol=golesf-golesc
        self.__golesF+=golesf
        self.__golesC+=golesc
        self.__difGol+=(diferencia_gol)
        if diferencia_gol==0:
            self.__puntos+=1
        elif diferencia_gol>0:
            self.__puntos+=3

    def __gt__(self,otro):
        """Metodo para sobrecargar el operador >"""
        if self.__puntos==otro.getPuntos_Equipo():
            if self.__difGol==otro.getDifGoles_Equipo():
                return self.__golesF > otro.getGolesF_Equipo()
            else:
                return self.__difGol > otro.getDifGoles_Equipo()
        else:
            return self.__puntos > otro.getPuntos_Equipo()

    def __del__(self):
        print("Se elimino el equipo ", self.__nombre_e)
