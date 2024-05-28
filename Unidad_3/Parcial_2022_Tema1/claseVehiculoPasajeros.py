from claseVehiculo import Vehiculo

class VehiculoPasajero(Vehiculo):
    __cantAsientos:int

    def __init__(self,cantA,**kwargs):
        super().__init__(kwargs['Marca'],kwargs['Modelo'],kwargs['Patente'],kwargs['ImpA'],kwargs['CantKM'])
        self.__cantAsientos=cantA

    def getCantidadAsientos(self):
        return self.__cantAsientos

    def getImporteTotalAlquiler(self):
        base=self.getImporteBasicoAlquiler()
        total=self.getImporteBasicoAlquiler()

        if self.getCantidadKmRecorrer()>100:
            total+=((1*(self.getCantidadKmRecorrer()//10))*base)/100

        if self.getCantidadAsientos()>4:
            total+=(1*base)/100

        return total

    def getTipo(self):
        return "Pasajero"