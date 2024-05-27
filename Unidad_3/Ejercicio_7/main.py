"""Ejercicio 7 / Unidad 3 - Ary Toro"""
from claseObjectEncoder import ObjectEncoder
from claseIInterfaz import IInterfaz
from claseListaAgentes import Lista

def interfaz(manejarInterfaz:IInterfaz,accion,agente=None,pos=None):
    if accion==1:
        manejarInterfaz.insertarElemento(agente,pos)
    elif accion==2:
        manejarInterfaz.agregarElemento(agente)
    else:
        manejarInterfaz.mostrarElemento()

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
[9] ADICIONAL. Listar personal con indices
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
            GA.listarAgentes()
        else:
            print("Opcion Invalida!")
        opcion=menu()
