""""Ejercicio 1 / Unidad 3 - Ary Toro"""
class Departamento:
    __idDepto:int
    __idEdificio:int
    __nombreProp:str
    __numeroPiso:int
    __numeroDepto:int
    __cantidadDormitorios:int
    __cantidadBanios:int
    __superficie:float

    def __init__(self,idE,idD,nom,nump,numd,canD,canB,sup):
        self.__idEdificio=idE
        self.__idDepto=idD
        self.__nombreProp=nom
        self.__numeroPiso=nump
        self.__numeroDepto=numd
        self.__cantidadDormitorios=canD
        self.__cantidadBanios=canB
        self.__superficie=sup

    def __str__(self):
        return f"ID Depto: {self.__idDepto}\nNombre Propietario: {self.__nombreProp}\nCantidad Baños: {self.__cantidadBanios}\nCantidad Dormitorios: {self.__cantidadDormitorios}\n"
    def getIdEdificio(self):
        return self.__idEdificio

    def getIdDepto(self):
        return self.__idDepto

    def getNombrePropietario(self):
        return self.__nombreProp

    def getNumeroPiso(self):
        return self.__numeroPiso

    def getNumeroDepartamento(self):
        return self.__numeroDepto

    def getCantidadDormitorios(self):
        return self.__cantidadDormitorios

    def getCantidadBanios(self):
        return self.__cantidadBanios

    def getSuperficie(self):
        return self.__superficie
