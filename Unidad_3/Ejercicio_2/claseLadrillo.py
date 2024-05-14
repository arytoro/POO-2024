"""Ejercicio 2 / Unidad 3 - Ary Toro"""
class Ladrillo:
    __alto=7
    __largo=25
    __ancho=15
    __cantidad:int
    __identificador:int
    __kgMatPrimUti:float
    __costo: float
    __materiales:list

    def __init__(self,cantidad,ide,kgmp,costo):
        self.__cantidad=cantidad
        self.__identificador=ide
        self.__kgMatPrimUti=kgmp
        self.__costo=costo
        self.__materiales=[]

    def agregarMaterial(self,material):
        if (material in self.__materiales)is False:
            self.__materiales.append(material)
            print(f"Al ladrillo {self.__identificador} se le agrega el material {material.getMaterial()}")
        else:
            print(f"No se agrega el material {material.getMaterial()} al ladrillo {self.__identificador} porque ya lo tiene")

    def getCantidad(self):
        return self.__cantidad

    def getIdentificador(self):
        return self.__identificador

    def getKgMateria(self):
        return self.__kgMatPrimUti

    def getCosto(self):
        return self.__costo

    def listarMateriales_CosyCar(self):
        if len(self.__materiales)>0:
            for unmaterial in self.__materiales:
                print(f"Material {unmaterial.getMaterial()} \n-> Costo: {unmaterial.getCostoAdicional()} \n-> Caracteristica: {unmaterial.getCaracteristicas()}\n")
        else:
            print("El ladrillo con esa ID no usa material refractario")

    def getCostoTotal(self):
        acum=self.__costo
        for unmaterial in self.__materiales:
            acum+=unmaterial.getCostoAdicional()
        return acum

    def getMateriales(self):
        retorna:str=""
        if len(self.__materiales)>0:
            for unmaterial in self.__materiales:
                retorna+=str(unmaterial.getMaterial())+", "
        return retorna

    def getCostosAdicionales(self):
        retorna:str=""
        if len(self.__materiales)>0:
            for unmaterial in self.__materiales:
                retorna+="$"+str(unmaterial.getCostoAdicional())+", "
        return retorna

    @classmethod
    def getAlto(cls):
        return cls.__alto

    @classmethod
    def getLargo(cls):
        return cls.__largo

    @classmethod
    def getAncho(cls):
        return cls.__ancho
