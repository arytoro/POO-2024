""""Ejercicio 1 / Unidad 3 - Ary Toro"""
from claseDepartamento import Departamento
class Edificio:
    __idEdificio:int
    __nombre:str
    __direccion:str
    __nombreEmpresa:str
    __cantidadPisos:int
    __cantidadDeptos:int
    __departamentos:list

    def __init__(self,idEd,nomEd,dir,nomEm,canP,canD):
        self.__idEdificio=idEd
        self.__nombre=nomEd
        self.__direccion=dir
        self.__nombreEmpresa=nomEm
        self.__cantidadPisos=canP
        self.__cantidadDeptos=canD
        self.__departamentos=[]

    def agregarDepartamento(self,xidD,xidE,xnom,xnump,xnumd,xcand,xcanb,xsup):
        self.__departamentos.append(Departamento(xidD,xidE,xnom,xnump,xnumd,xcand,xcanb,xsup))

    def getIdEdificio(self):
        return self.__idEdificio

    def getNombreEdificio(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getNombreEmpresa(self):
        return self.__nombreEmpresa

    def getCantidadPisos(self):
        return self.__cantidadPisos

    def getCantidadDeptos(self):
        return self.__cantidadDeptos

    def listarPropietariosDepartamentos(self):
        for undepartamento in self.__departamentos:
            print(f"Departamento {undepartamento.getIdDepto()} - {undepartamento.getNombrePropietario()}")

    def getSuperficieTotal(self):
        acum:float=0
        for undepartamento in self.__departamentos:
            acum+=undepartamento.getSuperficie()
        return acum

    def existePropietario(self,xnom):
        band=False
        i=0
        while band is False and i<len(self.__departamentos):
            if self.__departamentos[i].getNombrePropietario()==xnom:
                band= True
            else:
                i+=1
        return band

    def getSuperficieDeptosPropietario(self,xnom):
        acum=0.0
        for undepartamento in self.__departamentos:
            if undepartamento.getNombrePropietario()==xnom:
                acum+=undepartamento.getSuperficie()
        return acum
    
    def existeNumPiso(self,xnumP):
        band=False
        i=0
        while band is False and i<len(self.__departamentos):
            if self.__departamentos[i].getNumeroPiso()==xnumP:
                band= True
            else:
                i+=1
        return band

    def listarDepartamentosConCondiciones(self,xnumP):
        cont=0
        for undepartamento in self.__departamentos:
            if undepartamento.getNumeroPiso()==xnumP:
                if undepartamento.getCantidadBanios()>1 and undepartamento.getCantidadDormitorios()==3:
                    print(undepartamento)
                    cont+=1
        return cont
