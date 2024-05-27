"""Ejercicio 8 / Unidad 3 - Ary Toro"""
from claseObjectEncoder import ObjectEncoder
from claseListaAgentes import Lista
from claseIInterfaz import IInterfaz
from claseIDirector import IDirector
from claseITesorero import ITesorero

def interfaz(manejarInterfaz:IInterfaz,accion,agente=None,pos=None):
    if accion==1:
        manejarInterfaz.insertarElemento(agente,pos)
    elif accion==2:
        manejarInterfaz.agregarElemento(agente)
    else:
        manejarInterfaz.mostrarElemento()

def tesorero(manejarTesorero:ITesorero):
    try:
        xdni=int(input("Ingresa el DNI a buscar: "))
        manejarTesorero.gastosSueldoPorEmpleado(xdni)
    except ValueError:
        print("Error. Se esperaba un numero")

def menuParaDirector():
    accion=None
    try:
        accion=int(input("""
                [1] Modificar sueldo basico
                [2] Modificar porcentaje por cargo a docente
                [3] Modificiar porcentaje por categoria a personal de apoyo
                [4] Modificiar importe extra a un docente investigador
                [0] Salir de interfaz Director
                -> """))
    except ValueError:
        pass
    return accion

def director(manejarDirector:IDirector):
    accion=menuParaDirector()
    while accion!=0:
        if accion==1:
            try:
                xdni=int(input("Ingresa el DNI del agente: "))
                nuevoBasico=float(input("Ingresa su nuevo sueldo basico: "))
                manejarDirector.modificarBasico(xdni,nuevoBasico)
            except ValueError:
                print('Error. Se esperaba un numero')
        elif accion==2:
            try:
                xdni=int(input("Ingresa el DNI del Docente: "))
                nuevoPorcentaje=float(input("Ingresa su nuevo porcentaje por cargo: "))
                manejarDirector.modificarPorcentajeporcargo(xdni,nuevoPorcentaje)
            except ValueError:
                print('Error. Se esperaba un numero')
        elif accion==3:
            try:
                xdni=int(input("Ingresa el DNI del Personal de Apoyo: "))
                nuevoPorcentaje=float(input("Ingresa su nuevo porcentaje por categoria: "))
                manejarDirector.modificarPorcentajeporcategoria(xdni,nuevoPorcentaje)
            except ValueError:
                print('Error. Se esperaba un numero')
        elif accion==4:
            try:
                xdni=int(input("Ingresa el DNI del Docente Investigador: "))
                nuevoImporteExtra=float(input("Ingresa su nuevo importe extra: "))
                manejarDirector.modificarImporteExtra(xdni,nuevoImporteExtra)
            except ValueError:
                print('Error. Se esperaba un numero')
        else:
            print('Opcion Invalida')
        accion=menuParaDirector()
    print('...Saliendo de la interfaz Director')
        
def menu():
    op=None
    try:
        op=int(input("""
                            Menú de Opciones
[1] Insertar un agente en una posicion determinada de la lista
[2] Agregar un agente al final de la lista
[3] Mostrar el tipo de agente de una posicion
[4] Ingresa nombre de carrera para listar ordenadamente por nombre los Docentes Investigadores 
[5] Ingresa un area de inv para conocer la cantidad de Investigadores y Docentes Investigadores de dicha area
[6] Listar agentes de manera ordenada por apellido
[7] Ingresa una categoria de inv para listar Docentes Investigadores y conocer importe a solicitar al Ministerio
[8] Guardar cambios en personal.json
[9] Acceder como Tesorero
[10] Acceder como Director
[11] ADICIONAL. Listar personal con indices
[0] SALIR
    -> """))
    except ValueError:
        pass
    return op


if __name__=='__main__':
    jsonF=ObjectEncoder()
    GA=Lista()
    #Carga de agentes desde el JSON (ver clase ObjectEncoder)
    diccionario=jsonF.leerJSONArchivo('personal.json')
    GA=jsonF.decodificarDiccionario(diccionario)
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            try:
                indice=int(input("Indica la posicion a insertar: "))
                nuevoAgente=GA.crearAgente()
                if nuevoAgente is not None: #Si es None es porque se cancelo la operacion de carga
                    interfaz(IInterfaz(GA),opcion,nuevoAgente,indice)
            except ValueError:
                print("ERROR. Se esperaba un numero")

        elif opcion==2:
            nuevoAgente=GA.crearAgente()
            if nuevoAgente is not None: #Si es None es porque se cancelo la operacion de carga
                interfaz(IInterfaz(GA),opcion,nuevoAgente)
        elif opcion==3:
            interfaz(IInterfaz(GA),opcion)
        elif opcion==4:
            carreraOp4=input("Ingresa la carrera: ").strip().lower()
            GA.listarDocentesInvestigadores_PorCarrera(carreraOp4)
        elif opcion==5:
            areaoOp5=input("Ingresa el area de investigacion: ").strip().lower()
            GA.mostrarCantidadInvestigadoresDocentesInv_PorArea(areaoOp5)
        elif opcion==6:
            GA.listarAgentes_OrdenadosPorApellido()
        elif opcion==7:
            cateOp7=input("Ingresa la categoria (I, II, III, IV o V): ").strip().lower()
            while cateOp7 not in ("i","ii","iii","iv","v"):
                cateOp7=input("Categoria Invalida! Las opciones son I, II, III, IV o V: ")
            GA.listarDocentesInvestigadores_PorCategoria(cateOp7)
        elif opcion==8:
            d= GA.toJSON()
            jsonF.guardarJSONArchivo(d,'personal.json')
            print("Cambios guardados exitosamente!")
        elif opcion==9:
            user=input("Ingresa el usuario: ")
            if user!='uTesoreso':
                print('Usuario Invalido!')
            else:
                pwd=input("Ingresa la contraseña: ")
                if pwd!='ag@74ck':
                    print('Contraseña invalida!')
                else:
                    print('...Ingresando como tesorero')
                    tesorero(ITesorero(GA))
        elif opcion==10:
            user=input("Ingresa el usuario: ")
            if user!='uDirector':
                print('Usuario Invalido!')
            else:
                pwd=input("Ingresa la contraseña: ")
                if pwd!='ufC77#!1':
                    print('Contraseña invalida!')
                else:
                    print('...Ingresando como Director')
                    director(IDirector(GA))

        elif opcion==11:
            GA.listarAgentes()
        else:
            print("Opcion Invalida!")
        opcion=menu()
