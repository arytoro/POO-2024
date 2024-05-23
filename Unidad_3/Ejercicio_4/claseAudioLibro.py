"""Ejercicio 4 / Unidad 3 - Ary Toro"""
from clasePublicacion import Publicacion
class AudioLibro(Publicacion):
    __tiempoRep:int
    __nomNarrador:str

    def __init__(self,**kwargs):
        super().__init__(kwargs['tit'],kwargs['cate'],kwargs['precioB'])
        self.__tiempoRep=kwargs['tiempoRep']
        self.__nomNarrador=kwargs['nomNarra']

    def getTiempoRep(self):
        return self.__tiempoRep

    def getNomNarrador(self):
        return self.__nomNarrador

    def __str__(self):
        return f'Titulo: {super().getTitulo()}\n Tiempo de Reproduccion {self.getTiempoRep()}'
