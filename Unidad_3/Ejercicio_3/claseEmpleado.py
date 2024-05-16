"""Ejercicio 3 / Unidad 3 - Ary Toro"""

class Empleado:
    __nya:str
    __idE:int
    __puesto:str
    __matriculas:list

    def __init__(self,nya,ide,puesto):
        self.__nya=nya
        self.__idE=ide
        self.__puesto=puesto
        self.__matriculas=[]

    def matricular(self,unamatricula):
        self.__matriculas.append(unamatricula)

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
                duracion=unamatricula.getPrograma().getDuracion()
                print(f"  - {nombreC} -> Duracion: {duracion}")
        else:
            print("Ese empleado no esta matriculado en ningun programa")

    #def listarIDSEmpleado(self):
    #    for unamatricula in self.__matriculas:
    #        print(id(unamatricula))

    def getCantidadMatriculas(self):
        return len(self.__matriculas)
