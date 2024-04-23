"""Ejercicio 5 / Unidad 2 - Ary Toro"""
import csv
from claseEquipo import Equipo

class GestorDeEquipo:
    """Clase gestor de equipo"""
    __equipos:list

    def __init__(self):
        self.__equipos=[]

    def agregarEquipo(self,unequipo):
        """Metodo que agrega un equipo a la lista de equipos"""
        self.__equipos.append(unequipo)

    def test(self):
        """Metodo que lee los datos desde archivo csv"""
        archivo= open('equipos2024.csv')
        reader= csv.reader(archivo,delimiter=';')
        for fila in reader:
            self.agregarEquipo(Equipo(int(fila[0]),fila[1],int(fila[2]),int(fila[3]),int(fila[4])))
        archivo.close()

    def getIdPorNombre(self,nom):
        """Metodo que recibe el nombre de un equipo y retorna su ID"""
        i=0
        band=False
        while band is False and i<len(self.__equipos):
            if self.__equipos[i].getNombre_Equipo()==nom:
                idE=self.__equipos[i].getID_Equipo()
                band=True
            else:
                i+=1
        if band is True:
            return idE
        else:
            return -1

    def getIndice(self,idE):
        """Metodo que retorna el indice de un equipo a partir de la ID"""
        i=0
        band=False
        while band is False and i<len(self.__equipos):
            if self.__equipos[i].getID_Equipo()==idE:
                band=True
            else:
                i+=1
        return i

    def actualizar(self,datos):
        """Metodo que actualiza los datos de un equipo tras disputarse las fechas"""
        for unafecha in datos:
            #print(unafecha)
            idLocal=unafecha[0]
            idVisitante=unafecha[2]
            indiceLocal=self.getIndice(idLocal)
            indiceVistante=self.getIndice(idVisitante)
            self.__equipos[indiceLocal].updatePostFecha(unafecha[1],unafecha[3])
            self.__equipos[indiceVistante].updatePostFecha(unafecha[3],unafecha[1])

    def getPosicionesEquipos(self):
        """Metodo que retorna una lista con los datos de los equipos en orden actual"""
        lista=[]
        for unequipo in self.__equipos:
            equipoX=[]
            equipoX.append(unequipo.getID_Equipo())
            equipoX.append(unequipo.getNombre_Equipo())
            equipoX.append(unequipo.getGolesF_Equipo())
            equipoX.append(unequipo.getGolesC_Equipo())
            equipoX.append(unequipo.getDifGoles_Equipo())
            equipoX.append(unequipo.getPuntos_Equipo())
            lista.append(equipoX)
        return lista

    def mostrarTablaEquipos(self):
        """Muestra la tabla de equipos"""
        tabla=self.getPosicionesEquipos()
        print("        ID      Nombre           Datos")
        for unequipo in tabla:
            ide=unequipo[0]
            nom=unequipo[1]
            gf=unequipo[2]
            gc=unequipo[3]
            df=unequipo[4]
            pun=unequipo[5]
            print(f"        {ide}     {nom}     GF:{gf}    GC:{gc}    DG:{df}    Puntos:{pun}")

    def ordenar(self):
        """Metodo que ordena la tabla de posiciones"""
        self.__equipos=sorted(self.__equipos,reverse=True)

    def guardarCSV(self):
        """Metodo que guarda la tabla de posiciones ordenada en un archivo csv"""
        posiciones=self.getPosicionesEquipos()
        archivo=open("tposiciones.csv",mode='w',newline='')
        writer=csv.writer(archivo,delimiter=";")
        for fila in posiciones:
            writer.writerow(fila)
        archivo.close()
        print("Se guardaron los datos exitosamente!")

    def eliminarEquipo(self,idE):
        """Ejecuta el destructor de un equipo"""
        indice=self.getIndice(idE)
        del self.__equipos[indice]
