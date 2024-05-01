
class Puntaje:
    __dni:int
    __estilo:str
    __puntaje1:int
    __puntaje2:int
    __puntaje3:int

    def __init__(self,dni,estilo,p1,p2,p3):
        self.__dni=dni
        self.__estilo=estilo
        self.__puntaje1=p1
        self.__puntaje2=p2
        self.__puntaje3=p3
    
    def getEstilo(self):
        return self.__estilo

    def getDNI(self):
        return self.__dni
    
    def getPromedioPuntajeTotal(self):
        return (self.__puntaje1+self.__puntaje2+self.__puntaje3)/3
    
    def __gt__(self,otro):
        return self.getPromedioPuntajeTotal() > otro.getPromedioPuntajeTotal()
    
    def listarValoraciones(self):
        print("Puntaje 1: ",self.__puntaje1)
        print("Puntaje 2: ",self.__puntaje2)
        print("Puntaje 3: ",self.__puntaje3)