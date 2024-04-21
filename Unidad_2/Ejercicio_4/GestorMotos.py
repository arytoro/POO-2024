"""Ejercicio 4 / Unidad 2 - Ary Toro"""
import csv
from claseMoto import Moto

class GestorDeMotos:
    """Clase Gestor de Motos"""
    __listaMotos:list

    def __init__(self):
        """Metodo constructor de gestor de motos"""
        self.__listaMotos=[]

    def agregarMoto(self,unamoto):
        """Metodo para agregar moto al gestor"""
        self.__listaMotos.append(unamoto)

    def testMoto(self):
        """Metodo para crear/leer moto"""
        archivo= open('datosMotos.csv')
        reader= csv.reader(archivo,delimiter=';')
        for fila in reader:
            self.agregarMoto(Moto(fila[0],fila[1],fila[2],int(fila[3])))

        archivo.close()

    def patentesRegistradas(self):
        """Este metodo devuelve una lista con las patentes de todas las motos"""
        listaPatentes=[]
        for i in self.__listaMotos:
            listaPatentes.append(i.getPatente())
        return listaPatentes

    def getDatos(self,patente):
        """Devuelve los datos del conductor con determinada patente de moto"""
        i=0
        encontrado=False
        listaDatos=[]
        while encontrado is False and i<len(self.__listaMotos):
            if self.__listaMotos[i].getPatente()==patente:
                encontrado=True
                listaDatos.append(self.__listaMotos[i].getConductor())
                listaDatos.append(self.__listaMotos[i].getMarca())
                listaDatos.append(self.__listaMotos[i].getKilometraje())
            else:
                i+=1
        if encontrado is False:
            return -1
        else:
            return listaDatos
    
    def conductoresRegistrados(self):
        """Este metodo devuelve un lista con los nombres de todos los conductores"""
        listaConductores=[]
        for i in self.__listaMotos:
            listaConductores.append(i.getConductor())
        return listaConductores

if __name__=='__main__':
    listadoMotos=GestorDeMotos()
    listadoMotos.testMoto()
