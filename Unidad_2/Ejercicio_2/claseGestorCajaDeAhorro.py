"""Este documento contiene el ejercicio 1 de la unidad 1 11/04"""
from claseCajaDeAhorro import CajaDeAhorro

class GestorDeCajas:
    """Clase Gestora de cajas"""
    __cajas:list

    def __init__(self):
        """Metodo constructur de lista"""
        self.__cajas=[]

    def agregar(self,unacaja):
        """Metodo para agregar cajas a la lista"""
        self.__cajas.append(unacaja)

    def test(self):
        """Metodo para instanciar caja de ahorro"""
        for i in range(3):
            nc=input(f"Ingresa el numero de cuenta de la caja {i+1}: ")
            c= input("Ingresa su CUIL: ")
            a= input("Ingresa el nombre: ")
            n= input("Ingresa el apellido: ")
            s= float(input("Ingresa el saldo: "))
            self.agregar(CajaDeAhorro(nc,c,a,n,s))

    def mostrar_lista(self):
        """Metodo para mostrar_lista datos"""
        for i in self.__cajas:
            i.mostrar_datos()

    def extraer_lista(self,pos):
        """Metodo para realizar una extraccion en la posicion dada"""
        nuevo_estadoe=self.__cajas[pos].extraer(100)
        if nuevo_estadoe<0:
            print("Saldo insuficiente. No se puede realizar la extraccion")

    def depositar_lista(self,pos):
        """Metodo para realizar un deposito en la posicion dada"""
        self.__cajas[pos].depositar(200)

    def validar_cuil_lista(self,pos):
        """Metodo que analiza la validez de un cuil"""
        self.__cajas[pos].validar_cuil()

    def obtenerDatos(self,cuil):
        """Metodo para obtener los datos de una caja a partir de un cuil"""
        i=0
        encontrado=False
        datos=[]
        while encontrado is not True and i<len(self.__cajas):
            xcuil=self.__cajas[i].obtenerCUIL()
            if xcuil==cuil:
                encontrado=True
            else:
                i+=1
        if encontrado is True:
            xnombre=self.__cajas[i].obtenerNombre()
            xapellido=self.__cajas[i].obtenerApellido()
            xsueldo=self.__cajas[i].obtenerSaldo()
            datos.append(xnombre)
            datos.append(xapellido)
            datos.append(xsueldo)
            return datos
        else:
            return "El CUIL ingresado no pertenece a una caja de ahorra"


""" Lote de Prueba para la carga de datos
567
23-45472019-9
Toro
Cristian
500
910
20-45213500-1
Perez
Pablo
350.8
527
20-45378619-7
Rodriguez
Juan
1500
"""        