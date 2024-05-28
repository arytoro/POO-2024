
class Vehiculo:
    __marca:str
    __modelo:str
    __patente:str
    __importeB:float
    __cantidadKM:float

    def __init__(self,marca,modelo,patente,imp,cant):
        self.__marca=marca
        self.__modelo=modelo
        self.__patente=patente
        self.__importeB=imp
        self.__cantidadKM=cant

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getPatente(self):
        return self.__patente

    def getImporteBasicoAlquiler(self):
        return self.__importeB

    def getCantidadKmRecorrer(self):
        return self.__cantidadKM

    def getImporteTotalAlquiler(self):
        pass

    def getTipo(self):
        pass