"""Ejercicio 3 / Unidad 3 - Ary Toro"""
import gc
class GestorMatriculas:
    __listaMatriculas:list

    def __init__(self):
        self.__listaMatriculas=[]

    def agregarMatricula(self,unamatricula):
        self.__listaMatriculas.append(unamatricula)

    def listarMatriculas(self):
        for unamatricula in self.__listaMatriculas:
            print(unamatricula.getFecha(),"-> ",unamatricula.getEmpleado(),"se matriculo en ",unamatricula.getPrograma())

    def existeMatricula(self,unamatricula):
        band=False
        i=0
        while band is False and i<len(self.__listaMatriculas):
            if (unamatricula.getEmpleado()==self.__listaMatriculas[i].getEmpleado()) and (unamatricula.getPrograma()==self.__listaMatriculas[i].getPrograma()):
                band=True
            else:
                i+=1
        return band

    def borrarMatriculaPorIndice(self,indice):
        #self .__listaMatriculas[indice]=None
        del self.__listaMatriculas[indice]
        #gc.collect() Ahi te muestro

    def listarDireccionesMatriculas(self):
        for unamatricula in self.__listaMatriculas:
            print(id(unamatricula))
