from claseVehiculo import Vehiculo

class VehiculoCarga(Vehiculo):
    __pesoCarga:float

    def __init__(self,pesoCarga,**kwargs):
        super().__init__(kwargs['Marca'],kwargs['Modelo'],kwargs['Patente'],kwargs['ImpA'],kwargs['CantKM'])
        self.__pesoCarga=pesoCarga

    def getPesoCarga(self):
        return self.__pesoCarga

    def getImporteTotalAlquiler(self):
        base=self.getImporteBasicoAlquiler()
        total=self.getImporteBasicoAlquiler()

        if self.getCantidadKmRecorrer()>100:
            total+=((5*(self.getCantidadKmRecorrer()//10))*base)/100

        if self.getPesoCarga()>500:
            total+=((10*(self.getPesoCarga()//100))*base)/100

        return total
    
    def getTipo(self):
        return "Carga"
