
class Federado:
    __apellido:str
    __nombre:str
    __dni:int
    __edad:int
    __club:str

    def __init__(self,ape,nom,dni,edad,club):
        self.__apellido=ape
        self.__nombre=nom
        self.__dni=dni
        self.__edad=edad
        self.__club=club

    def getDNI(self):
        return self.__dni

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def getClub(self):
        return self.__club