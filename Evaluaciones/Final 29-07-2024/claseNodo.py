from claseClienteLocal import ClienteLocal

class Nodo:
    __cliente:ClienteLocal
    __siguiente:object

    def __init__(self,cliente):
        self.__cliente=cliente
        self.__siguiente=None

    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente
    def getCliente(self):
        return self.__cliente
    def getSiguiente(self):
        return self.__siguiente
