"""Ejercicio 7 / Unidad 3 - Ary Toro"""
from clasePersonal import Personal

class Docente(Personal):
    __carrera:str
    __cargo:str
    __catedra:str

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__carrera=kwargs['Carrera']
        self.__cargo=kwargs['Cargo']
        self.__catedra=kwargs['Catedra']

    def getCarrera(self):
        return self.__carrera

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra

    def getSueldoTotal(self):
        base=self.getSueldoBasico()
        total=self.getSueldoBasico()

        total+=(self.getAntiguedad()*base)/100
        
        if self.getCargo().strip().lower()=="simple":
            total+=(10*base)/100
        elif self.getCargo().strip().lower()=="semiexclusivo":
            total+=(20*base)/100
        elif self.getCargo().strip().lower()=="exclusivo":
            total+=(50*base)/100
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
                Carrera=self.getCarrera(),
                Cargo=self.getCargo(),
                Catedra=self.getCatedra(),
                Area="",
                Tipo=""
                )
            )
        return d
