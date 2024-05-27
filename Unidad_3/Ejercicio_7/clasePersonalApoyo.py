"""Ejercicio 7 / Unidad 3 - Ary Toro"""
from clasePersonal import Personal

class PersonalApoyo(Personal):
    __categoria:int
    def __init__(self,**kwargs):
        super().__init__(Cuil=kwargs['Cuil'],Ape=kwargs['Ape'],Nom=kwargs['Nom'],SueldoB=kwargs['SueldoB'],Antig=kwargs['Antig'],Categoria=super().__init__(Cuil=kwargs['Cuil'],Ape=kwargs['Ape'],Nom=kwargs['Nom'],SueldoB=kwargs['SueldoB'],Antig=kwargs['Antig'],Categoria=kwargs['Categoria']))
        self.__categoria=kwargs['Categoria']

    def getCategoria(self):
        return self.__categoria

    def getSueldoTotal(self):
        base=self.getSueldoBasico()
        total=self.getSueldoBasico()
        total+=(self.getAntiguedad()*base)/100

        if self.getCategoria()>=1 and self.getCategoria()<=10:
            total+=(10*base)/100
        elif self.getCategoria()>=11 and self.getCategoria()<=20:
            total+=(20*base)/100
        elif self.getCategoria()==21  or self.getCategoria()==22:
            total+=(30*base)/100
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
                Categoria=self.getCategoria()
                )
            )
        return d
