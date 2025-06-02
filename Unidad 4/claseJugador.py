"Unidad 4 - Ary Toro"
class Jugador:
    __nombre:str
    __puntaje:int
    __fecha:str
    __hora=str

    def __init__(self,Nombre='',Puntaje=0,Fecha='',Hora=''):
        self.__nombre=Nombre
        self.__puntaje=Puntaje
        self.__fecha=Fecha
        self.__hora=Hora

    def get_nombre(self):
        return self.__nombre

    def get_puntaje(self):
        return self.__puntaje

    def get_fecha(self):
        return self.__fecha

    def get_hora(self):
        return self.__hora

    def __gt__(self,otro):
        return self.get_puntaje() > otro.get_puntaje()

    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                Nombre=self.get_nombre(),
                Puntaje=self.get_puntaje(),
                Fecha=self.get_fecha(),
                Hora=self.get_hora(),
                )
            )
        return d
