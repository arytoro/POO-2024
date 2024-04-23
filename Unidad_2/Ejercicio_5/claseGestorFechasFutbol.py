"""Ejercicio 5 / Unidad 2 - Ary Toro"""
import csv
from claseFechaFutbol import FechaDeFutbol

class GestorDeFechas:
    """Clase gestor de fechas"""
    __partidos:list

    def __init__(self):
        self.__partidos=[]

    def agregarFecha(self,unpartido):
        """Metodo que agrega una fecha a la lista de fechas"""
        self.__partidos.append(unpartido)

    def test(self):
        """Metodo que lee los datos desde archivo csv"""
        archivo= open('fechasFutbol.csv')
        reader= csv.reader(archivo,delimiter=';')
        for fila in reader:
            self.agregarFecha(FechaDeFutbol(fila[0],int(fila[1]),int(fila[2]),int(fila[3]),int(fila[4])))
        archivo.close()

    def mostrarDatosEquipo(self,idEquipo,nombre):
        """Muestra datos de equipo y devuelve una lista"""
        acumGF=0
        acumGC=0
        acumPuntos=0
        print(f"""
                        Equipo: {nombre}
                        Fecha          GF      GC        DG    Puntos""")
        for unpartido in self.__partidos:
            jugo=False
            fecha=unpartido.getFecha_Partido()
            idLocal=unpartido.getIdLocal_Partido()
            idVisitante=unpartido.getIdVisitante_Partido()
            if (idLocal==idEquipo)is True:
                gf=unpartido.getGolesLocal_Partido()
                gc=unpartido.getGolesVisitante_Partido()
                jugo=True
            elif (idVisitante==idEquipo)is True:
                gf=unpartido.getGolesVisitante_Partido()
                gc=unpartido.getGolesLocal_Partido()
                jugo=True
            else:
                gf=0
                gc=0

            dg=gf-gc
            if dg==0:
                pun=1
            elif dg<0:
                pun=0
            else:
                pun=3

            if jugo is True:
                print(f"""
                        {fecha}     {gf}        {gc}        {dg}      {pun}
                """)
                acumGF+=gf
                acumGC+=gc
                acumPuntos+=pun

        print(f"""              ------------------------------------------------------------------
                        Total:         {acumGF}        {acumGC}        {acumGF-acumGC}      {acumPuntos}""")

    def getResultados(self):
        """Metodo que retorna una lista con los resultados de cada partido"""
        lista=[]
        for unpartido in self.__partidos:
            partidoX=[]
            partidoX.append(unpartido.getIdLocal_Partido())
            partidoX.append(unpartido.getGolesLocal_Partido())
            partidoX.append(unpartido.getIdVisitante_Partido())
            partidoX.append(unpartido.getGolesVisitante_Partido())
            lista.append(partidoX)
        return lista
