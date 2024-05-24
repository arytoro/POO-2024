"""Ejercicio 4 / Unidad 3 - Ary Toro"""
from clasePublicacion import Publicacion
class LibroImpreso(Publicacion):
    __nomAutor:str
    __fechaEdicion:str
    __cantPaginas:int

    def __init__(self,**kwargs):
        super().__init__(kwargs['tit'],kwargs['cate'],kwargs['precioB'])
        self.__nomAutor=kwargs['nomAutor']
        self.__fechaEdicion=kwargs['fechaEdi']
        self.__cantPaginas=kwargs['cantPag']

    def getNomAutor(self):
        return self.__nomAutor

    def getFechaEdicion(self):
        return self.__fechaEdicion

    def getCantPaginas(self):
        return self.__cantPaginas

    def getImporteVenta(self):
        anio=int(self.getFechaEdicion()[6:10]) #De la posicion 6 a 10 estan los numeros que corresponden al año
        importe=self.getPrecioBase() - ((2024-anio)*self.getPrecioBase())/100
        return importe

    def __str__(self):
        return f'Titulo: {super().getTitulo()}\n Nombre de Autor {self.getNomAutor()}'
