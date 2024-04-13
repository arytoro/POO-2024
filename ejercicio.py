"""Este documento contiene el ejercicio 1 de la unidad 1 11/04"""
from claseCA import CajaDeAhorro

class Lista:
    """Clase Lista de cajas"""
    __caja:list

    def __init__(self):
        """Metodo constructur de lista"""
        self.__caja=[]

    def agregar(self,uncaja):
        """Metodo para agregar cajas a la lista"""
        self.__caja.append(uncaja)

    def test(self):
        #Esta forma de instanciar esta mal, lo mejor seria trabajarlo con arreglos Numpy(aun no los he visto)
        # o combinando listas con diccionarios simulando un arreglo de registros(tengo entendido que no
        # trabajamos con diccionarios en este curso)
        """Metodo para instanciar caja de ahorro"""
        nc1=input('Ingresa el numero de cuenta de caja 1:' )
        c1=input('Ingresa su CUIL:' )
        a1=input("Ingresa su apellido: ")
        n1=input("Ingresa su nombre: ")
        s1=float(input("Ingresa saldo: "))
        caja1= CajaDeAhorro(nc1,c1,a1,n1,s1)

        nc2=input('Ingresa el numero de cuenta de caja 2:' )
        c2=input('Ingresa su CUIL:' )
        a2=input("Ingresa su apellido: ")
        n2=input("Ingresa su nombre: ")
        s2=float(input("Ingresa saldo: "))
        caja2= CajaDeAhorro(nc2,c2,a2,n2,s2)

        nc3=input('Ingresa el numero de cuenta de caja 3:' )
        c3=input('Ingresa su CUIL:' )
        a3=input("Ingresa su apellido: ")
        n3=input("Ingresa su nombre: ")
        s3=float(input("Ingresa saldo: "))
        caja3= CajaDeAhorro(nc3,c3,a3,n3,s3)

        self.agregar(caja1)
        self.agregar(caja2)
        self.agregar(caja3)

    def mostrar_lista(self):
        """Metodo para mostrar_lista datos"""
        for i in self.__caja:
            i.mostrar_datos()

    def extraer_lista(self,pos):
        """Metodo para realizar una extraccion en la posicion dada"""
        nuevo_estadoe=self.__caja[pos].extraer(100)
        if nuevo_estadoe<0:
            print("Saldo insuficiente. No se puede realizar la extraccion")

    def depositar_lista(self,pos):
        """Metodo para realizar un deposito en la posicion dada"""
        self.__caja[pos].depositar(200)

    def validar_cuil_lista(self,pos):
        """Metodo que analiza la validez de un cuil"""
        self.__caja[pos].validar_cuil()

def principal():
    """Main del programa"""
    lista_cajas=Lista()
    lista_cajas.test()
    lista_cajas.mostrar_lista()
    lista_cajas.extraer_lista(1)
    lista_cajas.depositar_lista(0)
    lista_cajas.validar_cuil_lista(1)


if __name__=="__main__":
    principal()

"""
567
23-45472019-9
Toro
Cristian
500
910
20-45213500-1
Tejada
Cesar
350.8
523
20-45378619-7
Reinoso
Mateo
1500
"""        