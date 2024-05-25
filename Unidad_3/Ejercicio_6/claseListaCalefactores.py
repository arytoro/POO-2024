"""Ejercicio 6 / Unidad 3 - Ary Toro"""
from claseNodo import Nodo
from claseIInterfaz import IInterfaz,implementer
from claseCalefactorElectrico import CalefactorElectrico
from claseCalefactorGas import CalefactorGas

@implementer(IInterfaz)
class Lista:
    __comienzo:Nodo
    __actual:Nodo
    __indice:int
    __tope:int
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato= self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def __getTope(self):
        return self.__tope

    def crearCalefactor(self):
        nuevoCalefactor=None
        tipo=int(input("Que Tipo?\n   [1] Electrico\n   [2] Gas\n   [0] Cancelar\n   -> "))
        while (tipo in (1,2,0))is False:
            tipo=int(input("Tipo invalido!\n   [1] Electrico\n   [2] Gas\n   [0] Cancelar\n   -> "))
        if tipo!=0:
            marca=input("Ingresa la marca: ").strip()
            modelo=input("Modelo: ")
            pais=input("Pais de Fabricacion: ")
            precio=float(input("Precio de Lista: "))

            forma=input("Forma de Pago (contado/cuotas): ").strip().lower() #Strip permite borrar los espacios sobrantes en blanco, y el lower convierte todo a minusculas
            while (forma in ('contado','cuotas','cuota'))is False: #Que itere hasta que se ingrese: contado o cuotas o cuota
                forma=input("Forma de Pago Invalida. Escribe contado o cuotas: ").strip().lower()
            if forma=='contado':
                cuotas=1
            else:
                cuotas=int(input("Cantidad de Cuotas: "))

            promo=input("Promocion (si/no): ").strip().lower()
            while (promo in ('si','no'))is False: #Que itere hasta que se ingrese: si o no
                promo=input("Eleccion invalida. Esta en promocion? (si/no): ").strip().lower()

            if tipo==1:
                potencia=int(input("Potencia Maxima(en watts): "))
                nuevoCalefactor=CalefactorElectrico(Marca=marca,Modelo=modelo,PaisF=pais,Precio=precio,FPago=forma,CCuotas=cuotas,Promo=promo,PotenciaM=potencia)
            else:
                matricula=input("Matricula: ")
                calorias=int(input("Calorias(en kcal/m3): "))
                nuevoCalefactor=CalefactorGas(Marca=marca,Modelo=modelo,PaisF=pais,Precio=precio,FPago=forma,CCuotas=cuotas,Promo=promo,Matricula=matricula,Calorias=calorias)
        return nuevoCalefactor

    def insertarElemento(self,nuevoCalefactor,pos):
        try:
            if pos > self.__getTope(): #El indice solo puede variar entre 0 y la cantidad de nodos
                raise IndexError #Si es mayor, debe emitir una excepecion de IndexError

            nuevoNodo=Nodo(nuevoCalefactor)
            if pos==0:
                #Si la posicion es 0, se debe insertar por la cabeza
                nuevoNodo.setSiguiente(self.__comienzo)
                self.__comienzo=nuevoNodo
                self.__actual=nuevoNodo
                self.__tope+=1
                print("Insertado exitosamente\n")
            else:
                #Sino es 0, se debe recorrer hasta alcanzar dicho indice
                aux=self.__comienzo
                anterior=self.__comienzo
                indice=0
                while (aux is not None) and (pos != indice):
                    anterior=aux
                    aux=aux.getSiguiente()
                    indice+=1
                anterior.setSiguiente(nuevoNodo)
                nuevoNodo.setSiguiente(aux)
                self.__actual=self.__comienzo
                self.__tope+=1
                print("Insertado exitosamente\n")
        except IndexError:
            print("ERROR. El indice excede a la lista. Debe variar entre 0 y",self.__getTope())

    def agregarElemento(self,nuevoCalefactor):
        nuevoNodo=Nodo(nuevoCalefactor)
        if self.__comienzo is None:
            self.__comienzo=nuevoNodo
        else:
            aux=self.__comienzo
            while aux is not None:
                anterior=aux
                aux=aux.getSiguiente()
            anterior.setSiguiente(nuevoNodo)
        self.__actual=self.__comienzo
        self.__tope+=1
        print("Agregado exitosamente!\n")

    def mostrarElemento(self):
        try:
            pos=int(input("Ingresa la posicion en la lista: "))
            if pos >= self.__getTope():
                raise IndexError
            else:
                cont=0
                band=False
                aux=self.__comienzo
                while aux!=None and band is False:
                    if pos==cont:
                        if isinstance(aux.getDato(),CalefactorElectrico):
                            print(f"El calefactor de marca {aux.getDato().getMarca()} y modelo {aux.getDato().getModelo()} es del tipo Calefactor Electrico")
                        else:
                            print(f"El calefactor de marca {aux.getDato().getMarca()} y modelo {aux.getDato().getModelo()} es del tipo Calefactor Gas")
                        band=True
                    else:
                        aux=aux.getSiguiente()
                        cont+=1

        except ValueError:
            print("ERROR. Se esperaba un numero")
        except IndexError:
            print("ERROR. El indice ingresado no es valido, debe variar entre 0 y",self.__getTope()-1)

    def mostrarDatosCalefactorGas_MenorPrecio(self):
        minimo=999999999
        auxMin=None
        print("----- Datos del Calefactor a Gas Natural mas barato -----")
        for uncalefactor in self:
            if isinstance(uncalefactor,CalefactorGas) and uncalefactor.getPrecio()<minimo:
                minimo=uncalefactor.getPrecio()
                auxMin=uncalefactor
        print(f"Marca: {auxMin.getMarca()}\nModelo: {auxMin.getModelo()}\nPrecio: {minimo}\n")

    def mostrarDatosCalefactorElectrico_PorMarca(self):
        band=False
        xmarca=input("Ingresa la marca del calefactor: ")
        for uncalefactor in self:
            if isinstance(uncalefactor,CalefactorElectrico) and uncalefactor.getMarca().lower() == xmarca.lower(): #El lower convierte todo a minusculas
                print(f"Modelo: {uncalefactor.getModelo()}\nPotencia: {uncalefactor.getPotenciaMax()}\nPrecio de lista: {uncalefactor.getPrecio()}\n")
                band=True
        if band is False:
            print("No existen calefactores electricos con dicha marca")

    def mostrarDatosCalefactores_EnPromocion(self):
        band=False
        for uncalefactor in self:
            if uncalefactor.getPromocion() == 'si':
                print(f"""
                    Marca: {uncalefactor.getMarca()}
                    Modelo: {uncalefactor.getModelo()}
                    Pais de Fabricacion: {uncalefactor.getPaisFabrica()}
                    Importe de Venta: {uncalefactor.getImporteVenta()}\n""")
                band=True
        if band is False:
            print("No existen calefactores en promocion")

    def listarCalefactores(self):
        cont=0
        for uncalefactor in self:
            if isinstance(uncalefactor,CalefactorElectrico):
                print(cont,"-",uncalefactor.getPrecio()," Electrico")
            else:
                print(cont,"-",uncalefactor.getPrecio()," Gas")
            cont+=1

    def toJSON(self):
        d= dict(
            __class__=self.__class__.__name__,
            calefactores=[calefactor.toJSON() for calefactor in self]
            )
        return d
