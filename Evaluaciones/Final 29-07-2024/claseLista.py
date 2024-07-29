from claseClienteLocal import ClienteLocal
from claseClienteNacional import ClienteNacional
from claseNodo import Nodo
class Lista:
    __comienzo:Nodo
    __actual:Nodo
    __indice:int
    __tope:int
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato= self.__actual.getCliente()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def agregarCliente(self,uncliente):
        nuevoNodo=Nodo(uncliente)
        if self.__comienzo is None:
            self.__comienzo=nuevoNodo
        else:
            aux=self.__comienzo
            while aux is not None:
                anterior=aux
                aux=aux.getSiguiente()
            anterior.setSiguiente(nuevoNodo)
        self.__actual=self.__comienzo
        self.__tope+=1
        print("Agregado exitosamente!\n")

    def listarClientesNacionales(self):
        i=0
        print("Indice - Nombre del Cliente - Nombre de Provincia")
        for uncliente in self:
            if isinstance(uncliente,ClienteNacional):
                print(f"{i} - {uncliente.getNombre()} - {uncliente.getProvincia()}")
            i+=1

    def mostrarTipoCliente(self,xindice):
        if xindice < self.__tope:
            aux=self.__comienzo
            for i in range(xindice):
                aux=aux.getSiguiente()
            if isinstance(aux.getCliente(),ClienteNacional):
                print("El cliente de dicha posicion es de la clase Cliente Nacional")
            elif isinstance(aux.getCliente(),ClienteLocal):
                print("El cliente de dicha posicion es de la clase Cliente Local")
        else:
            raise IndexError

    def listarTodo(self):
        for uncliente in self:
            print(uncliente)
