import abc
from abc import ABC
class Vehiculo(ABC):
    __marca:str
    __modelo:str
    __anioF:int
    __capacidadP:int
    __numPlazas:int
    __distRecorrida:float
    __tarifaBase:float

    def __init__(self,marca,modelo,anio,capP,numP,distR,tarB):
        self.__marca=marca
        self.__modelo=modelo
        self.__anioF=anio
        self.__capacidadP=capP
        self.__numPlazas=numP
        self.__distRecorrida=distR
        self.__tarifaBase=tarB

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getAnioFab(self):
        return self.__anioF

    def getCapacidadP(self):
        return self.__capacidadP
    
    def getNumPlazas(self):
        return self.__numPlazas

    def getDistanciaR(self):
        return self.__distRecorrida

    def getTarifaBase(self):
        return self.__tarifaBase

    @abc.abstractmethod
    def getTarifaTotal(self):
        pass

    def __str__(self):
        return f"""
                ° Modelo: {self.getModelo()}
                  Anio Fabricacion: {self.getAnioFab()}
                  Capacidad de Pasajeros: {self.getCapacidadP()}
                  Tarifa del Servicio: {self.getTarifaTotal()}"""
