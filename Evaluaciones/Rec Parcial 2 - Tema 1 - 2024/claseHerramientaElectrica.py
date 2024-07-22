"""Recuperatorio Parcial 2 - Tema 1 - 2024 / Ary Toro"""
from claseEquipo import Equipo

class HerramientaElectrica(Equipo):
    __tipoAli:str

    def __init__(self,mar,mod,anio,tipo,pote,cap,tar,dias,tipoAli):
        super().__init__(mar,mod,anio,tipo,pote,cap,tar,dias)
        self.__tipoAli=tipoAli

    def getTipoAlimentacion(self):
        return self.__tipoAli

    def getTarifaAlquilerTotal(self):
        total=self.getTarifaAlquilerDiario() * self.getDiasAlquiler()
        if self.getTipoAlimentacion()=="bateria":
            total= total + (10 * total)/100

        return total

