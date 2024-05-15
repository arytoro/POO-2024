"""Ejercicio 2 / Unidad 3 - Ary Toro"""
import csv
import random
from claseLadrillo import Ladrillo

class GestorDeLadrillos:
    __listaLadrillos:list

    def __init__(self):
        self.__listaLadrillos=[]

    def agregarLadrillo(self,unladrillo):
        self.__listaLadrillos.append(unladrillo)

    def cargarLadrillos(self):
        band=False
        archivo=open("ladrillos.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if band is False:
                band=True
            else:
                self.agregarLadrillo(Ladrillo(int(fila[0]),int(fila[1]),float(fila[2]),float(fila[3])))
        archivo.close()

    def asignarMateriales(self,GM):
        """Lo hice aleatorio para probar funciones, la asignacion de materiales se podria hacer manual"""
        indicesLadrillos=list(range(len(self.__listaLadrillos))) #Aqui tengo una lista con los indices de todos los ladrillos en la lista
        indicesMateriales=list(range(GM.getTotalMateriales()))  #Aqui tengo una lista con los indices de todos los materiales en el gestor de materiales
        for i in range(4): #Quiero que asigne metaeriales 4 vaces de manera aleatorio
            indiceRandomL=random.choice(indicesLadrillos)  #Choice toma uno de los indice de ladrillos
            indiceRandomM=random.choice(indicesMateriales) #Este lo mismo pero con un indice de material
            self.__listaLadrillos[indiceRandomL].agregarMaterial(GM.getMaterialPorPosicion(indiceRandomM))
    
    def mostrarDatosMateriales(self,xid):
        band=False
        i=0
        while band is False and i<len(self.__listaLadrillos):
            if self.__listaLadrillos[i].getIdentificador()==xid:
                self.__listaLadrillos[i].listarMateriales_CosyCar()
                band=True
            else:
                i+=1
        assert band is True

    def mostrarCostosTotalDeFabricacion(self):
        for unladrillo in self.__listaLadrillos:
            print(f"Ladrillo {unladrillo.getIdentificador()} -> Costo Total De Fabricacion: ",unladrillo.getCostoTotal())

    def mostrarDetallesLadrillos(self):
        print("             N° Identidicador          Material                     Costo Adicional")
        for unladrillo in self.__listaLadrillos:
            xid=unladrillo.getIdentificador()
            xmat=unladrillo.getMateriales()
            if xmat != "":
                xcosto=unladrillo.getCostosAdicionales()
                print(f"""
                    {xid}                      {xmat}                           {xcosto}
                      """)
            else:
                print(f"""
                    {xid}                      -                                -""")
