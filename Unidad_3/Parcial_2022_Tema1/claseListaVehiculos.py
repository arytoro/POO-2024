from claseNodo import Nodo
from claseVehiculoCarga import VehiculoCarga
from claseVehiculoPasajeros import VehiculoPasajero

class Lista:
    __comienzo:Nodo
    __actual:Nodo
    __indice:int
    __tope:int
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato= self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def __getTope(self):
        return self.__tope

    def agregarVehiculo(self,nuevoVehiculo):
        nuevoNodo=Nodo(nuevoVehiculo)
        nuevoNodo.setSiguiente(self.__comienzo)
        self.__comienzo=nuevoNodo
        self.__actual=nuevoNodo
        self.__tope+=1
        print("Insertado exitosamente\n")

    def mostrarDatosVehiculosPasajeros(self):
        for unvehiculo in self:
            if isinstance(unvehiculo,VehiculoPasajero) and unvehiculo.getCantidadAsientos()>6:
                print(f"""
                ° Patente: {unvehiculo.getPatente()}
                  Marca: {unvehiculo.getMarca()}
                  Modelo: {unvehiculo.getModelo()}
                  Importe Basico de Alquiler: {unvehiculo.getImporteBasicoAlquiler()}
                  Cantidad de KM a recorrer: {unvehiculo.getCantidadKmRecorrer()}
                  Cantidad de Asientos: {unvehiculo.getCantidadAsientos()}
                  Importe Total de Alquiler: {unvehiculo.getImporteTotalAlquiler()}""")

    def mostrarCantidadVehiculosCarga(self,xmarca):
        cont=0
        for unvehiculo in self:
            if isinstance(unvehiculo,VehiculoCarga) and unvehiculo.getMarca().strip().lower()==xmarca:
                cont+=1
        print(f"En total hay {cont} vehiculos de carga de la marca ingresada")

    def listarVehiculos(self):
        print("""
        Marca                Modelo           Tipo de Vehiculo     KM a Recorrer       Total Alquiler""")
        for unvehiculo in self:
            marca=unvehiculo.getMarca().zfill(15).replace("0"," ")
            modelo=unvehiculo.getModelo().zfill(20).replace("0"," ")
            tipo=unvehiculo.getTipo().zfill(20).replace("0"," ")
            km=str(unvehiculo.getCantidadKmRecorrer()).replace("0","ñ").zfill(20).replace("0"," ").replace("ñ","0")
            ita=str(unvehiculo.getImporteTotalAlquiler()).replace("0","ñ").zfill(18).replace("0"," ").replace("ñ","0")
            print(marca,modelo,tipo,km,ita)

            