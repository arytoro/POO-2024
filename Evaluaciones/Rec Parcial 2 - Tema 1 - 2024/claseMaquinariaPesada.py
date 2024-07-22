"""Recuperatorio Parcial 2 - Tema 1 - 2024 / Ary Toro"""
from claseEquipo import Equipo

class MaquinariaPesada(Equipo):
    __tipoMaq:str
    __peso:float

    def __init__(self,mar,mod,anio,tipo,pote,cap,tar,dias,tipoMaq,peso):
        super().__init__(mar,mod,anio,tipo,pote,cap,tar,dias)
        self.__tipoMaq=tipoMaq
        self.__peso=peso

    def getTipoMaquinaria(self):
        return self.__tipoMaq

    def getPeso(self):
        return self.__peso

    def getTarifaAlquilerTotal(self):
        total=self.getTarifaAlquilerDiario() * self.getDiasAlquiler()

        if self.getPeso()>10:
            total= total + (20 * total)/100

        return total
