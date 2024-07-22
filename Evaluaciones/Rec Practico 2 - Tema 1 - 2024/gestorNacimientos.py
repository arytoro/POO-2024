"""Recuperatio Practico 2 - Tema 1 - 2024 / Ary Toro"""
import csv
from claseNacimiento import Nacimiento

class GestorDeNacimientos:
    __listaNacimientos:list

    def __init__(self):
        self.__listaNacimientos=[]

    def agregarNacimiento(self,unnacimiento):
        self.__listaNacimientos.append(unnacimiento)

    def cargarNacimientos(self):
        band=True
        archivo=open("Nacimientos.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if band is True:
                band=False
            else:
                self.agregarNacimiento(Nacimiento(int(fila[0]),fila[1],fila[2],fila[3],float(fila[4].replace(",",".")),float(fila[5])))
        archivo.close()

    def getTipo_porDNI(self,xdni):
        band=False
        i=0
        tipo=None
        while band is False and i<len(self.__listaNacimientos):
            if self.__listaNacimientos[i].getDNI()==xdni:
                tipo=self.__listaNacimientos[i].getTipo()
                band=True
            else:
                i+=1
        return tipo

    def listarBebes_porDNI(self,xdni):
        for unbebe in self.__listaNacimientos:
            if unbebe.getDNI()==xdni:
                print(f"""
                      Peso          Altura
                      {unbebe.getPeso()}            {unbebe.getAltura()}""")

    def detectar_partos_multiples(self,GM):
        longitud_lista=len(self.__listaNacimientos)
        listadas=[] #Guarda las madres que ya se mostraron para no repetirlas dos veces
        for i in range(longitud_lista):
                for j in range(longitud_lista):
                    par_valido_1=[]
                    par_valido_1.append(i)
                    par_valido_1.append(j)
                    par_valido_2=[]
                    par_valido_2.append(j)
                    par_valido_2.append(i)
                    if i!=j and (((par_valido_1 or par_valido_2) in listadas) is False) and(self.__listaNacimientos[i]==self.__listaNacimientos[j]):
                        listadas.append(par_valido_1)
                        listadas.append(par_valido_2)
                        GM.listar_mamas_partos_multiples(self.__listaNacimientos[i].getDNI())

