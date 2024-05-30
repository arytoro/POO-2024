from claseVehiculo import Vehiculo

class Autobus(Vehiculo):
    __tipoS:str
    __turnoS:str

    def __init__(self,marca,modelo,anio,capP,numP,distR,tarB,tipoS,turnoS):
        super().__init__(marca,modelo,anio,capP,numP,distR,tarB)
        self.__tipoS=tipoS
        self.__turnoS=turnoS

    def getTipoServicio(self):
        return self.__tipoS

    def getTurnoServicio(self):
        return self.__turnoS

    def getTarifaTotal(self):
        base=self.getTarifaBase()
        total=self.getTarifaBase()

        if self.getTurnoServicio()=='noche' and self.getTipoServicio()=='turismo':
            total+=(20*base)/100
        else:
            total+=(5*base)/100

        return total
