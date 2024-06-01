import csv
from claseAutobus import Autobus
from claseVan import Van

class GestorVehiculos:
    __listaVehiculos=[]

    def __init__(self):
        self.__listaVehiculos:list

    def agregarVehiculo(self,unvehiculo):
        self.__listaVehiculos.append(unvehiculo)

    def cargarArchivosCSV(self):
        band=False
        archivo=open('vehiculos.csv',encoding="UTF-8")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if band is False:
                band=True
            else:
                if fila[0]=='A':
                    self.agregarVehiculo(Autobus(fila[1],fila[2],int(fila[3]),int(fila[4]),int(fila[5]),float(fila[6]),float(fila[7]),fila[8],fila[9]))
                elif fila[0]=='V':
                    self.agregarVehiculo(Van(fila[1],fila[2],int(fila[3]),int(fila[4]),int(fila[5]),float(fila[6]),float(fila[7]),fila[8]))
        archivo.close()

    def mostrarTipoVehiculo_PorIndice(self,xindice):
        if xindice<len(self.__listaVehiculos):
            if isinstance(self.__listaVehiculos[xindice],Autobus):
                print("Es del tipo Autobus")
            elif isinstance(self.__listaVehiculos[xindice],Van):
                print("Es del tipo Van")
        else:
            raise IndexError

    def mostrarCantidadVehiculos_PorTipos(self):
        contA=0
        contV=0
        for unvehiculo in self.__listaVehiculos:
            if isinstance(unvehiculo,Autobus):
                contA+=1
            elif isinstance(unvehiculo,Van):
                contV+=1
        print(f"La cantidad de Autobuses es {contA}")
        print(f"La cantidad de Vanes es {contV}")

    def listarDatosVehiculos(self):
        for unvehiculo in self.__listaVehiculos:
            print(unvehiculo)
