"""Ejercicio 3 / Unidad 3 - Ary Toro"""

class Matricula:
    __fecha:str
    __empleado:object
    __programa:object

    def __init__(self,fecha,empleado,programa):
        self.__fecha=fecha
        self.__empleado=empleado
        self.__programa=programa

    def getFecha(self):
        return self.__fecha

    def getEmpleado(self):
        return self.__empleado

    def getPrograma(self):
        return self.__programa


    def __del__(self):
        print("Se elimino la matricula de ",self.__empleado)
