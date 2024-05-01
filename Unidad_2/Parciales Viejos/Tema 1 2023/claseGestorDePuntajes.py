import csv
from clasePuntaje import Puntaje

class GestorDePuntajes:
    __lista_puntajes:list

    def __init__(self):
        self.__lista_puntajes=[]
    
    def agregarPuntaje(self,unpuntaje):
        self.__lista_puntajes.append(unpuntaje)
        
    def test(self):
        band:bool=False
        i:int=0
        archivo=open('evaluaciones.csv')
        reader= csv.reader(archivo,delimiter=";")
        for fila in reader:
            if band is False:
                band= True
            else:
                self.agregarPuntaje(Puntaje(int(fila[0]),fila[1],int(fila[2]),int(fila[3]),int(fila[4])))
    
    
    def mostrarDatosMejorPuntaje(self,GF):
        xestilo:str
        xdni:int
        long:int
        band:bool=False
        i:int=0
        max=Puntaje(-1,"",-1,-1,-1)
        for unpuntaje in self.__lista_puntajes:
            if unpuntaje>max:
                max=unpuntaje

        xestilo=max.getEstilo()
        xdni=max.getDNI()
        long=len(GF._GestorDeFederados__lista_federados)

        while band is False and i<long:
            if GF._GestorDeFederados__lista_federados[i].getDNI()==xdni:
                print("----- Datos del patinador con mejor puntaje: ------")
                print("APELLIDO: ",GF._GestorDeFederados__lista_federados[i].getApellido())
                print("NOMBRE: ",GF._GestorDeFederados__lista_federados[i].getNombre())
                print("CLUB: ",GF._GestorDeFederados__lista_federados[i].getClub())
                print("ESTILO: ",xestilo)
                band=True
            else:
                i+=1

    def listarPatinadoresPorEstilo(self,GF):
        xdni:int
        print("Patinadores con Estilo Libre y Estilo Escuela: ")
        for unpuntaje in self.__lista_puntajes:
            if unpuntaje.getEstilo()=="L":
                xdni=unpuntaje.getDNI()
            for otropuntaje in self.__lista_puntajes:
                if otropuntaje.getEstilo()=='E' and otropuntaje.getDNI()==xdni:
                    GF.mostrarTodosLosDatos_porDNI(xdni)

        
    def mostrarValoraciones(self):
        xdni:int
        band:bool=False
        i:int=0
        xdni= int(input("Ingresa el DNI del patinador: "))
        xestilo= input("Ingresa el estilo: ")
        while band is False and i<len(self.__lista_puntajes):
            if xdni==self.__lista_puntajes[i].getDNI():
                self.__lista_puntajes[i].listarValoraciones()
                band=True
            else:
                i+=1
        if band is False:
            print("No existe el DNI ingresado")