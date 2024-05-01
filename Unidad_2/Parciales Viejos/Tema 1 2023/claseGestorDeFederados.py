import csv
from claseFederado import Federado

class GestorDeFederados:
    __lista_federados:list

    def __init__(self):
        self.__lista_federados=[]

    def agregarFederado(self,unfederado):
        self.__lista_federados.append(unfederado)

    def test(self):
            band:bool=False
            i:int=0
            archivo=open('federados.csv')
            reader= csv.reader(archivo,delimiter=";")
            for fila in reader:
                if band is False:
                    band= True
                else:
                    self.agregarFederado(Federado(fila[0],fila[1],int(fila[2]),int(fila[3]),fila[4]))
    
    def mostrarApellidoNombre_porDNI(self,dni):
        band:bool=False
        i:int=0
        while band is False and i<(len(self.__lista_federados)):
            if self.__lista_federados[i].getDNI()==dni:
                print("°Nombre: ",self.__lista_federados[i].getNombre())
                print("°Apellido: ",self.__lista_federados[i].getApellido())
                print("°DNI: ",dni)
                band= True
            else:
                i+=1
            
    def listarDatosPorEstilo(self,GP):
        estilo_x:str
        dni_x:int
        longitud:int
        estilo_x=input('Ingresa el estilo L=Libre E=Escuela: ')
        edad=int(input("Ingresa su edad: "))
        longitud=len(GP._GestorDePuntajes__lista_puntajes)
        for i in range(longitud):
            if GP._GestorDePuntajes__lista_puntajes[i].getEstilo()==estilo_x:
                dni_x=GP._GestorDePuntajes__lista_puntajes[i].getDNI()
                self.mostrarApellidoNombre_porDNI(dni_x)

    def mostrarTodosLosDatos_porDNI(self,dni):
        band:bool=False
        i:int=0
        while band is False and i<(len(self.__lista_federados)):
            if self.__lista_federados[i].getDNI()==dni:
                print("°Nombre: ",self.__lista_federados[i].getNombre())
                print("°Apellido: ",self.__lista_federados[i].getApellido())
                print("°DNI: ",dni)
                print("°Edad: ",self.__lista_federados[i].getEdad())
                print("°Club: ",self.__lista_federados[i].getClub())
                band= True
            else:
                i+=1
