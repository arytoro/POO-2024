"""Ejercicio 8 / Unidad 3 - Ary Toro"""
from clasePersonal import Personal

class Docente(Personal):
    __carrera:str
    __cargo:str
    __catedra:str
    __porcentajePCargo:float

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__carrera=kwargs['Carrera']
        self.__cargo=kwargs['Cargo']
        self.__catedra=kwargs['Catedra']
        self.__porcentajePCargo=kwargs['PorcCargo']
        
    def getCarrera(self):
        return self.__carrera

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra

    def getPorcentajePCargo(self):
        return self.__porcentajePCargo
    
    def setPorcentajePCargo(self,nuevoPorc):
        self.__porcentajePCargo=nuevoPorc

    def getSueldoTotal(self):
        base=self.getSueldoBasico()
        total=self.getSueldoBasico()

        total+=(self.getAntiguedad()*base)/100
        
        total+=(self.getPorcentajePCargo()*base)/100

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
                PorcCargo=self.getPorcentajePCargo(),
                Area="",
                Tipo=""
                )
            )
        return d