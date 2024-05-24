"""Ejercicio 4 / Unidad 3 - Ary Toro"""
import csv
from claseNodo import Nodo
from claseAudioLibro import AudioLibro
from claseLibroImpreso import LibroImpreso

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
            dato= self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def __getTope(self):
        return self.__tope

    def cargarPublicaciones(self):
        band1= False
        band2= False
        archivo1=open("libros.csv")
        reader1=csv.reader(archivo1,delimiter=";")
        for fila1 in reader1:
            if band1 is False:
                band1=True
            else:
                self.agregarPublicacion(LibroImpreso(tit=fila1[0],cate=fila1[1],precioB=float(fila1[2]),nomAutor=fila1[3],fechaEdi=fila1[4],cantPag=int(fila1[5])))
        archivo1.close()

        archivo2=open("cd.csv")
        reader2=csv.reader(archivo2,delimiter=";")
        for fila2 in reader2:
            if band2 is False:
                band2=True
            else:
                self.agregarPublicacion(AudioLibro(tit=fila2[0],cate=fila2[1],precioB=float(fila2[2]),tiempoRep=int(fila2[3]),nomNarra=fila2[4]))
        archivo2.close()

    def agregarPublicacion(self,publicacion):
        nodo= Nodo(publicacion)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
        print("Cargado Exitosamente!")

    def getTipoPublicacion(self,pos):
        if pos<= self.__getTope()-1: #El tope tiene la cantidad de nodos en la lista
            aux=self.__comienzo
            for i in range(pos):
                aux=aux.getSiguiente()
            if isinstance(aux.getDato(),AudioLibro):
                print(f'{aux.getDato().getTitulo()} es del tipo Audio-Libro')
            elif isinstance(aux.getDato(),LibroImpreso):
                print(f'{aux.getDato().getTitulo()} es del tipo Libro Impreso')
        else:
            print('Indice invalido. Solo puede variar entre 0 y ',self.__getTope()-1)

    def mostrarCantidadPorTipo(self):
        cont1=0
        cont2=0
        aux=self.__comienzo
        while aux is not None:
            if isinstance(aux.getDato(),LibroImpreso):
                cont1+=1
            elif isinstance(aux.getDato(),AudioLibro):
                cont2+=1
            aux=aux.getSiguiente()
        #Ya que la lista esta codificada como un iterador, tambien se podria recorrer con un for. Tal cual los muestro en la funcion de abajo
        print(f"Hay {cont1} publicaciones de libro impreso. Y {cont2} de audio-libro")

    def mostrarPublicaciones(self):        
        for unapublicacion in self:
            precioBase= unapublicacion.getPrecioBase()
            if isinstance(unapublicacion,LibroImpreso):
                anio=unapublicacion.getFechaEdicion()[6:10] #De la posicion 6 a 10 estan los numeros que corresponden al año
                importe= precioBase - ((2024-int(anio))*precioBase)/100
            elif isinstance(unapublicacion,AudioLibro):
                importe=precioBase + (10*precioBase)/100

            print(f'°Titulo: {unapublicacion.getTitulo()}\n Categoria: {unapublicacion.getCategoria()}\n Importe de Venta: {round(importe,2)}\n')

    def listarPublicacionesConIndice(self):
        indice=0
        for unapublicacion in self:
            print(indice," - ",unapublicacion.getTitulo())
            indice+=1
