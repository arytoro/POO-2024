"""Recuperatio Practico 2 - Tema 1 - 2024 / Ary Toro"""
class Nacimiento:
    __dni:int
    __tipo:str
    __fecha:str
    __hora:str
    __peso:float
    __altura:float

    def __init__(self,d,t,f,h,p,a):
        self.__dni=d
        self.__tipo=t
        self.__fecha=f
        self.__hora=h
        self.__peso=p
        self.__altura=a

    def getDNI(self):
        return self.__dni

    def getTipo(self):
        return self.__tipo

    def getFecha(self):
        return self.__fecha
    
    def getHora(self):
        return self.__hora

    def getPeso(self):
        return self.__peso

    def getAltura(self):
        return self.__altura

    def __eq__(self,otro):
        return (self.getDNI() == otro.getDNI()) and (self.getFecha() == otro.getFecha())