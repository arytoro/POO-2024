"""Ejercicio 3 / Unidad 3 - Ary Toro"""
from claseMatricula import Matricula
class Empleado:
    __nya:str
    __idE:int
    __puesto:str
    __matriculas:list
    __fecha="14/05/2024"
    __contMatriculas=0

    def __init__(self,nya,ide,puesto):
        self.__nya=nya
        self.__idE=ide
        self.__puesto=puesto
        self.__matriculas=[]

    def matricular(self,unprograma,GM):
        fecha=self.getFecha()
        nuevaMatricula= Matricula(fecha,self,unprograma)
        if GM.existeMatricula(nuevaMatricula) is False: #Porque al ser al azar puede salir repetida. Evito q se duplique
            GM.agregarMatricula(nuevaMatricula)
            unprograma.matricular(nuevaMatricula)
            self.__matriculas.append(nuevaMatricula)
            self.incrementarContador()
            print(f"Se matriculo a {self.__nya} en el programa {unprograma.getNombre()}")
        else:
            print(f"No se matriculo a {self.__nya} en el programa {unprograma.getNombre()}. Pues ya estaba matriculado")
#Cuando elimino una instancia de matricula, sigue apareceniendo en los gestores de las que sale. Hice pruebas con los IDS de memoria y tienen la misma ID
    def getNyA(self):
        return self.__nya

    def getID(self):
        return self.__idE

    def getPuesto(self):
        return self.__puesto

    def __str__(self):
        return f"{self.__nya} ({self.__idE})"
    
    def listarDuracionProgramas(self):
        if len(self.__matriculas)>0:
            print(f"{self.__nya} está matriculado en: ")
            for unamatricula in self.__matriculas:
                nombreC=unamatricula.getPrograma().getNombre()
                duracion=unamatricula.getPrograma().getDuracion() #No eso nomas era. Gracias!
                print(f"  - {nombreC} -> Duracion: {duracion}")
        else:
            print("Ese empleado no esta matriculado en ningun programa")

    def getCantidadMatriculas(self):
        return self.getContador()

    @classmethod
    def getContador(cls):
        return cls.__contMatriculas

    @classmethod
    def incrementarContador(cls):
        cls.__contMatriculas+=1

    @classmethod
    def getFecha(cls):
        return cls.__fecha

    @classmethod
    def setFecha(cls,xfecha):
        cls.__fecha=xfecha
