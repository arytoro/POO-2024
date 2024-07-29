class ClienteLocal:
    __nombre:str
    __apellido:str
    __email:str
    __contrasenia:str
    __direccionPostal:str
    __telefono:int

    def __init__(self,nombre,apellido,email,contrasenia,direccionPostal,telefono):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__email=email
        self.__contrasenia=contrasenia
        self.__direccionPostal=direccionPostal
        self.__telefono=telefono

    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getEmail(self):
        return self.__email
    def getContrasenia(self):
        return self.__contrasenia
    def getDireccionPostal(self):
        return self.__direccionPostal
    def getTelefono(self):
        return self.__telefono

    def __str__(self):
        return f"""
            -> Nombre: {self.getNombre()}
               Apellido: {self.getApellido()}
               Email: {self.getEmail()}
               Contrasenia: {self.getContrasenia()}
               Direccion Postal: {self.getDireccionPostal()}
               Telefono: {self.getTelefono()}"""