"""Recuperatio Practico 2 - Tema 1 - 2024 / Ary Toro"""
class Madre:
    __dni:int
    __edad:int
    __ayn:str

    def __init__(self,d,e,a):
        self.__dni=d
        self.__edad=e
        self.__ayn=a

    def getDNI(self):
        return self.__dni

    def getEdad(self):
        return self.__edad

    def getAyN(self):
        return self.__ayn