"""Ejercicio 3 / Unidad 3 - Ary Toro"""
from random import choice
from claseMatricula import Matricula
class GestorMatriculas:
    __listaMatriculas:list
    __fecha="16/05/2024"

    def __init__(self):
        self.__listaMatriculas=[]

    def agregarMatricula(self,unamatricula):
        self.__listaMatriculas.append(unamatricula)
    
    def existeMatricula(self,unamatricula):
        band=False
        i=0
        while band is False and i<len(self.__listaMatriculas):
            if (unamatricula.getEmpleado()==self.__listaMatriculas[i].getEmpleado()) and (unamatricula.getPrograma()==self.__listaMatriculas[i].getPrograma()):
                band=True
            else:
                i+=1
        return band

    def asignarMatriculaciones(self,GE,GP):
        indicesEmpleados=list(range(GE.getCantidadEmpleados()))
        indicesProgramas=list(range(GP.getCantidadProgramas()))
        for i in range(5):
            iE=choice(indicesEmpleados)#Tomo al azar un indice de empleado y otro de un programa
            iP=choice(indicesProgramas)
            nuevaMatricula=Matricula(self.getFecha(),GE.getEmpleadoPorIndice(iE),GP.getProgramaPorIndice(iP))

            if self.existeMatricula(nuevaMatricula) is False:
                self.agregarMatricula(nuevaMatricula)
                GE.getEmpleadoPorIndice(iE).matricular(nuevaMatricula)
                GP.getProgramaPorIndice(iP).matricular(nuevaMatricula)
                print(f"Se matriculó a {GE.getEmpleadoPorIndice(iE)} en el programa {GP.getProgramaPorIndice(iP)}")
            else:
                print(f"No se matriculó a {GE.getEmpleadoPorIndice(iE)} en el programa {GP.getProgramaPorIndice(iP)} pues ya estaba matriculado")


    def listarMatriculas(self):
        for unamatricula in self.__listaMatriculas:
            print(unamatricula.getFecha(),"-> ",unamatricula.getEmpleado(),"se matriculo en ",unamatricula.getPrograma())


    def borrarMatriculaPorIndice(self,indice):
        del self.__listaMatriculas[indice]

    #def mostrarIDSMatriculas(self):
    #    for unamatricula in self.__listaMatriculas:
    #        print(id(unamatricula))

    @classmethod
    def getFecha(cls):
        return cls.__fecha

    @classmethod
    def setFecha(cls,xfecha):
        cls.__fecha=xfecha
