"""Ejercicio 4 / Unidad 2 - Ary Toro"""
import csv
from clasePedido import Pedido
from GestorMotos import GestorDeMotos

class GestorDePedido:
    """Clase Gestor de Pedidos"""
    __listaPedidos:list

    def __init__(self):
        """Metodo constructor de gestor de pedidos"""
        self.__listaPedidos=[]

    def agregarPedido(self,unpedido):
        """Metodo para agregar pedido al gestor"""
        self.__listaPedidos.append(unpedido)

    def testPedido(self):
        """Metodo para crear/leer pedido"""
        archivo= open('datosPedidos.csv')
        reader= csv.reader(archivo,delimiter=';')
        for fila in reader:
            self.agregarPedido(Pedido(fila[0],int(fila[1]),fila[2],int(fila[3]),float(fila[4]),int(fila[5])))
        archivo.close()

    def ordenar(self):
        """Metodo para ordenar la lista de pedidos en orden ascendente en base a patente"""
        #print(self.__listaPedidos) #Antes de ordenar
        self.__listaPedidos=sorted(self.__listaPedidos)
        #print(self.__listaPedidos) #Despues de ordenar

    def nuevoPedido(self,patentes):
        """Metodo que agrega un nuevo pedido"""
        patente_nueva=input("Ingresa la patente del conductor: ")
        while (patente_nueva in patentes) is False:
            print("Patente invalida, ingresa una de las siguientes: ", patentes)
            patente_nueva=input("-> ")
        id=int(input("ID: "))
        comida=input("Comida: ")
        te= int(input("Tiempo estimado de entrega (minutos): "))
        precio=float(input("Precio: "))
        self.agregarPedido(Pedido(patente_nueva,id,comida,te,precio))
        print("...Carga Exitosa!")

    def modificarTiempoReal(self):
        """Metodo que modifica el tiempo real de entrega de un pedido"""
        i=0
        encontrado=False
        p=input('Ingresa la patente: ')
        id= int(input('ID: '))
        while encontrado is False and i<len(self.__listaPedidos):
            if self.__listaPedidos[i].getID()==id:
                tr= int(input('Nuevo tiempo real (en minutos): '))
                self.__listaPedidos[i].setTiempoReal(tr)
                encontrado=True
            else:
                i+=1
        if encontrado is False:
            print('La ID del pedido no existe')

    def mostrarDatosyProm(self,motos):
        """Metodo que devuelve datos del conductor y promedio de tiempo real de entrega"""
        acum=0
        cont=0
        p=input("Ingresa la patente del conductor: ")
        datos=motos.getDatos(p)
        if datos!=-1:
            for unpedido in self.__listaPedidos:
                if unpedido.getPatente()==p:
                    acum+=unpedido.getTiempoReal()
                    cont+=1
            print('El nombre del conductor es ',datos[0])
            print('Maneja una moto de la marca ',datos[1]," cuyo kilometraje es ",datos[2])
            print('Su promedio de tiempo real de entrega es ',acum/cont)
        else:
            print("La patente ingresada no existe")
    
    def calcularComisiones(self,patentes,conductores):
        """Muestra y calcula las comisiones para cada moto"""
        long=len(patentes)
        for i in range(long):
            acum=0
            xpat=patentes[i]
            xcon=conductores[i]
            print(f"""      °Comisiones para moto {i+1}
                    Patente de la moto: {xpat}
                    Conductor: {xcon}
                    ID de Pedido      Tiempo Estimado     Tiempo Real     Precio""")
            for unpedido in self.__listaPedidos:
                if unpedido.getPatente()==xpat:
                    xid= unpedido.getID()
                    xte= unpedido.getTiempoEstimado()
                    xtr= unpedido.getTiempoReal()
                    xpr= unpedido.getPrecio()
                    acum+=xpr
                    print(f"""
                        {xid}                 {xte}                {xtr}         ${xpr}""")
            print(f"""
                    Total: ${round(acum,2)}
                    Comisión: ${round((20*acum)/100,2)}""")
            print("------------------")
