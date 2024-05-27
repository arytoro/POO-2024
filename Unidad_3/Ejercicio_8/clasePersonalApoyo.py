"""Ejercicio 7 / Unidad 3 - Ary Toro"""
from clasePersonal import Personal

class PersonalApoyo(Personal):
    __categoria:int
    __porcentajePCate:float
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__categoria=kwargs['Categoria']
        self.__porcentajePCate=kwargs['PorcCate']

    def getCategoria(self):
        return self.__categoria

    def getPorcentajePCate(self):
        return self.__porcentajePCate

    def setPorcentajePCate(self,nuevoPorc):
        self.__porcentajePCate=nuevoPorc

    def getSueldoTotal(self):
        base=self.getSueldoBasico()
        total=self.getSueldoBasico()
        total+=(self.getAntiguedad()*base)/100
        total+=(self.getPorcentajePCate()*base)/100
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
                Categoria=self.getCategoria(),
                PorcCate=self.getPorcentajePCate()
                )
            )
        return d
