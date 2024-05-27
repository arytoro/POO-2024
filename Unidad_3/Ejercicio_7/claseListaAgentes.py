"""Ejercicio 7 / Unidad 3 - Ary Toro"""
from claseNodo import Nodo
from claseIInterfaz import IInterfaz,implementer
from claseDocenteInvestigador import DocenteInvestigador,Docente,Investigador
from clasePersonalApoyo import PersonalApoyo

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

    def crearAgente(self):
        nuevoAgente=None
        try:
            tipo=int(input("Que Tipo?\n   [1] Docente\n   [2] Investigador\n   [3] De Apoyo\n   [4] Docente Investigador\n   -> "))
            while (tipo in (1,2,3,4,0))is False:
                tipo=int(input("Tipo invalido!\n   [1] Docente\n   [2] Investigador\n   [3] De Apoyo\n   [4] Docente Investigador\n   -> "))
            if tipo!=0:
                cuil=input("Ingresa su CUIL: ")
                ape=input("Apellido: ")
                nom=input("Nombre: ")
                sueldob=float(input("Sueldo Basico: "))
                antig=int(input("Antiguedad (en años): "))

                if tipo==1:
                    carrera=input("Carrera en la que dicta clases: ")

                    cargo=input("Cargo (Simple,Semiexclusivo o Exclusivo): ")
                    while cargo.strip().lower() not in ('simple','semiexclusivo','exclusivo'):#Itera hasta que se ingresa uno de los tres cargos
                        cargo=input("Cargo Invalido! Las opciones son Simple,Semiexclusivo o Exclusivo): ")

                    catedra=input("Catedra: ")
                    nuevoAgente=Docente(Cuil=cuil,Ape=ape,Nom=nom,SueldoB=sueldob,Antig=antig,Carrera=carrera,Cargo=cargo,Catedra=catedra,Area="",Tipo=" ")
                elif tipo==2:
                    area=input("Area de Investigacion: ")
                    tipoI=input("Tipo de Investigacion: ")
                    nuevoAgente=Investigador(Cuil=cuil,Ape=ape,Nom=nom,SueldoB=sueldob,Antig=antig,Carrera="",Cargo="",Catedra="",Area=area,Tipo=tipoI)
                elif tipo==3:
                    cate=int(input("Categoria (1 al 22): "))
                    while cate<=0 or cate>22: #Itera hasta que ingresa una categoria [1...22]
                        cate=int(input("Categoria Invalida! Solo puede variar entre 1 y 22: "))
                    nuevoAgente=PersonalApoyo(Cuil=cuil,Ape=ape,Nom=nom,SueldoB=sueldob,Antig=antig,Categoria=cate)
                else:
                    carrera=input("Carrera en la que dicta clases: ")
                    cargo=input("Cargo (Simple, Semiexclusivo o Exclusivo): ")
                    while cargo.strip().lower() not in ('simple','semiexclusivo','exclusivo'):#Itera hasta que ingresa uno de los 3 cargos
                        cargo=input("Cargo Invalido! Las opciones son Simple,Semiexclusivo o Exclusivo): ")
                    catedra=input("Catedra: ")
                    area=input("Area de Investigacion: ")
                    tipoI=input("Tipo de Investigacion: ")
                    cateI=input("Categoria de Incentivo (I,II,III,IV o V): ")
                    while cateI.strip().lower() not in ('i','ii','iii','iv','v'):#Itera hasta que ingresa una de las 5 categorias
                        cateI=input("Categoria Invalida! Las opciones son I, II, III, IV o V: ")
                    impExtra=float(input("Importe Extra: "))
                    nuevoAgente=DocenteInvestigador(Cuil=cuil,Ape=ape,Nom=nom,SueldoB=sueldob,Antig=antig,Carrera=carrera,Cargo=cargo,Catedra=catedra,Area=area,Tipo=tipoI,CateI=cateI,ImpExtra=impExtra)
        except ValueError:
            print("Error. Se esperaba un numero")
        return nuevoAgente

    def insertarElemento(self,nuevoAgente,pos):
        #Inserta entre nodos
        try:
            if pos > self.__getTope(): #El indice solo puede variar entre 0 y la cantidad de nodos
                raise IndexError #Si es mayor, debe emitir una excepcion de IndexError

            nuevoNodo=Nodo(nuevoAgente)
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

    def agregarElemento(self,nuevoAgente):
        #Inserta al final de la lista
        nuevoNodo=Nodo(nuevoAgente)
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
            if pos >= self.__getTope(): #Si el indice es mayor o igual a la cantidad de nodos; sobrepasa a los indices de la lista y se emite un IndexError
                raise IndexError
            else:
                cont=0
                band=False
                aux=self.__comienzo
                while aux!=None and band is False:
                    if pos==cont:
                        if isinstance(aux.getDato(),DocenteInvestigador):
                            print(f"El personal de CUIL {aux.getDato().getCuil()} es del tipo Docente Investigador")
                        elif isinstance(aux.getDato(),Investigador):
                            print(f"El personal de CUIL {aux.getDato().getCuil()} es del tipo Investigador")
                        elif isinstance(aux.getDato(),PersonalApoyo):
                            print(f"El personal de CUIL {aux.getDato().getCuil()} es del tipo Personal de Apoyo")
                        elif isinstance(aux.getDato(),Docente):
                            print(f"El personal de CUIL {aux.getDato().getCuil()} es del tipo Docente")
                        band=True
                    else:
                        aux=aux.getSiguiente()
                        cont+=1

        except ValueError:
            print("ERROR. Se esperaba un numero")
        except IndexError:
            print("ERROR. El indice ingresado no es valido, debe variar entre 0 y",self.__getTope()-1)

    def __ordenarLista_PorCriterio(self,criterio):
        #Ordena la lista enlazada en funcion del atributo recibido por 'criterio'.
        #En el ordenamiento de abajo se utiliza el ordenamiento por burbuja mejorado
        cota=None
        k=None
        datoDelActual=None
        datoDelSiguiente=None
        while k!=self.__comienzo:
            k=self.__comienzo
            actual=self.__comienzo
            while actual.getSiguiente()!=cota:
                if criterio=='Nombre':
                    #Si el criterio a ordenar es por Nombre; Necesito comparar el Nombre del nodo actual con el Nombre del Nodo siguiente (item 4)
                    datoDelActual=actual.getDato().getNombre()
                    datoDelSiguiente=actual.getSiguiente().getDato().getNombre()
                elif criterio=='Apellido':
                    #Aca adaptado por si el criterio es Apellido (item 6)
                    datoDelActual=actual.getDato().getApellido()
                    datoDelSiguiente=actual.getSiguiente().getDato().getApellido()
                    #Aqui hago la comparacion, y en funcion de la validez, se intercambian o no.
                if datoDelActual > datoDelSiguiente:
                    aux=actual.getSiguiente().getDato()
                    #Para intercambiar los contenidos de los nodos, es necesario implementar el metodo setDato en la clase Nodo
                    actual.getSiguiente().setDato(actual.getDato())
                    actual.setDato(aux)
                    k=actual
                actual=actual.getSiguiente()
            cota=k.getSiguiente()
        print("Lista ordenada exitosamente!")

    def listarDocentesInvestigadores_PorCarrera(self,xcarre):
        self.__ordenarLista_PorCriterio('Nombre') #Aqui especifico que el criterio para el ordenamiento sea a traves del nombre del agente
        band=False
        for unagente in self:
            if isinstance(unagente,DocenteInvestigador) and unagente.getCarrera().strip().lower()==xcarre:
                print(unagente)
                band=True
        if band is False:
            print("No existen Docentes Investigadores que dicten esa carrera")

    def mostrarCantidadInvestigadoresDocentesInv_PorArea(self,xarea):
        cont1=0
        cont2=0
        for unagente in self:
            if isinstance(unagente,DocenteInvestigador) and unagente.getArea().strip().lower()==xarea:
                cont1+=1
            elif isinstance(unagente,Investigador) and unagente.getArea().strip().lower()==xarea:
                cont2+=1
        print(f"Cantidad de Docentes Investigadores: {cont1}\nCantidad de Investigadores: {cont2}")

    def listarAgentes_OrdenadosPorApellido(self):
        self.__ordenarLista_PorCriterio("Apellido")#Aqui especifico que el criterio para el ordenamiento sea a traves del apellido del agente
        tipo=None
        for unagente in self:
            if isinstance(unagente,DocenteInvestigador):
                tipo='Docente Investigador'
            elif isinstance(unagente,Docente):
                tipo= 'Docente'
            elif isinstance(unagente,Investigador):
                tipo= 'Investigador'
            elif isinstance(unagente,PersonalApoyo):
                tipo= 'Personal de Apoyo'
                
            print(f"""
                ° Apellido: {unagente.getApellido()}
                  Nombre: {unagente.getNombre()}
                  Tipo de Agente: {tipo}
                  Sueldo Total: {unagente.getSueldoTotal()}""")
            

    def listarDocentesInvestigadores_PorCategoria(self,xcate):
        total=0
        for unagente in self:
            if isinstance(unagente,DocenteInvestigador) and unagente.getCategoriaIncentivo().strip().lower() == xcate:
                print(f"""
                      ° Apellido: {unagente.getApellido()}
                        Nombre: {unagente.getNombre()}
                        Importe Extra por Docencia e Investigacion: {unagente.getImporteExtra()}""")
                total+=unagente.getImporteExtra()
        print(f"\nPara la categoria {xcate.upper()} se le debera solicitar al Ministerio la suma de ${total}")

    def listarAgentes(self):
        cont=0
        for unagente in self:
            if isinstance(unagente,DocenteInvestigador):
                print(cont,"-",unagente.getCuil()," Docente Investigador")
            elif isinstance(unagente,Investigador):
                print(cont,"-",unagente.getCuil()," Investigador")
            elif isinstance(unagente,PersonalApoyo):
                print(cont,"-",unagente.getCuil()," Apoyo")
            elif isinstance(unagente,Docente):
                print(cont,"-",unagente.getCuil()," Docente")
            cont+=1

    def toJSON(self):
        d= dict(
            __class__=self.__class__.__name__,
            agentes=[personal.toJSON() for personal in self]
            )
        return d
