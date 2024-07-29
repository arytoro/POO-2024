from claseClienteLocal import ClienteLocal

class ClienteNacional(ClienteLocal):
    __provincia:str
    __localidad:str
    __codigoPostal:str

    def __init__(self,nombre,apellido,email,contrasenia,direccionPostal,telefono,provincia,localidad,codigoPostal):
        super().__init__(nombre,apellido,email,contrasenia,direccionPostal,telefono)
        self.__provincia=provincia
        self.__localidad=localidad
        self.__codigoPostal=codigoPostal

    def getProvincia(self):
        return self.__provincia
    def getLocalidad(self):
        return self.__localidad
    def getCodigoPostal(self):
        return self.__codigoPostal


    def __str__(self):
        print(super().__str__())
        return f"""               Provincia: {self.getProvincia()}
               Localidad: {self.getLocalidad()}
               Codigo Postal: {self.getCodigoPostal()}"""
