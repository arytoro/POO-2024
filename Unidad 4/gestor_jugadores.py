"Unidad 4 - Ary Toro"
class GestorJugadores:
    __lista:list

    def __init__(self):
        self.__lista=[]

    def agregarJugador(self,unjugador):
        self.__lista.append(unjugador)

    def get_cantidad_jugadores(self):
        return len(self.__lista)

    def ordenar_jugadores(self):
        self.__lista.sort(reverse=True)

    def get_jugador(self,pos):
        return self.__lista[pos]

    def toJSON(self):
        d= dict(
            __class__=self.__class__.__name__,
            jugadores=[jugador.toJSON() for jugador in self.__lista]
            )
        return d
