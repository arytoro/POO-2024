from claseVehiculo import Vehiculo

class Van(Vehiculo):
    __tipoC:str

    def __init__(self,marca,modelo,anio,capP,numP,distR,tarB,tipoC):
        super().__init__(marca,modelo,anio,capP,numP,distR,tarB)
        self.__tipoC=tipoC

    def getTipoCarroceria(self):
        return self.__tipoC

    def getTarifaTotal(self):
        base=self.getTarifaBase()
        total=self.getTarifaBase()

        if self.getTipoCarroceria()=='minivan':
            total-=(10*base)/100
        else:
            total+=(2.5*base)/100

        return total
