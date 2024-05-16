"""Ejercicio 3 / Unidad 3 - Ary Toro"""
from claseMatricula import Matricula
class ProgramaCapacitacion:
    __nombre:str
    __codigo:str
    __duracion:int
    __matriculas:list
    __fecha="14/05/2024"

    def __init__(self,nom,cod,dur):
        self.__nombre=nom
        self.__codigo=cod
        self.__duracion=dur
        self.__matriculas=[]

    def matricular(self,unamatricula):
        self.__matriculas.append(unamatricula)

    def getNombre(self):
        return self.__nombre

    def getCodigo(self):
        return self.__codigo

    def getDuracion(self):
        return self.__duracion

    def __str__(self):
        return f"{self.__codigo}"

    def listarEmpleados(self):
        if len(self.__matriculas)>0:
            print("Empleado/s matriculado/s: ")
            for unamatricula in self.__matriculas:
                print(f" -{unamatricula.getEmpleado()}")
        else:
            print("No existen empleados matriculados en ese programa")

    @classmethod
    def getFecha(cls):
        return cls.__fecha

    @classmethod
    def setFecha(cls,xfecha):
        cls.__fecha=xfecha
