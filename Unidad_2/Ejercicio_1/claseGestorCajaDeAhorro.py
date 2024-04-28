"""Ejercicio 1 / Unidad 2 - Ary Toro"""
from claseCajaDeAhorro import CajaDeAhorro

class GestorDeCajas:
    """Clase GestorDeCajas de cajas"""
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
        nuevo_estadoe=self.__cajas[pos].extraer(100) #Se hará una extraccion de $100
        if nuevo_estadoe<0:
            print("Saldo insuficiente. No se puede realizar la extraccion")

    def depositar_lista(self,pos):
        """Metodo para realizar un deposito en la posicion dada"""
        self.__cajas[pos].depositar(200)    #Se depositaran $200

    def validar_cuil_lista(self,pos):
        """Metodo que analiza la validez de un cuil"""
        self.__cajas[pos].validar_cuil()
