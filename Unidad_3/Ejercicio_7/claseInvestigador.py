"""Ejercicio 7 / Unidad 3 - Ary Toro"""
from clasePersonal import Personal

class Investigador(Personal):
    __area:str
    __tipo:str

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__area=kwargs['Area']
        self.__tipo=kwargs['Tipo']

    def getArea(self):
        return self.__area

    def getTipo(self):
        return self.__tipo

    def getSueldoTotal(self):
        base=self.getSueldoBasico()
        total=self.getSueldoBasico()
        total+=(self.getAntiguedad()*base)/100
        return total

    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                Cuil=self.getCuil(),
                Ape=self.getApellido(),
                Nom=self.getNombre(),
                SueldoB=self.getSueldoBasico(),
                Antig=self.getAntiguedad(),
                Carrera="",
                Cargo="",
                Catedra="",
                Area=self.getArea(),
                Tipo=self.getTipo(),
                )
            )
        return d
