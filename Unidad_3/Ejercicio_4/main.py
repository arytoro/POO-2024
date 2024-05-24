"""Ejercicio 4 / Unidad 3 - Ary Toro"""
from claseListaPublicaciones import Lista
from claseLibroImpreso import LibroImpreso
from claseAudioLibro import AudioLibro
def menu():
    op=None
    try:
        op=int(input("""
                            Menú de Opciones
            [1] Agregar una publicacion
            [2] Conocer tipo de publicacion a partir de su posicion
            [3] Mostrar cantidad de publicaciones de cada tipo
            [4] Mostrar datos de las publicaciones
            [5] ADICIONAL. Listar libros con sus indices
            [0] SALIR
            -> """))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    GP=Lista()
    GP.cargarPublicaciones()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            try:
                tipoOp1=int(input('Tipo: [1] Libro Impreso [2] Audio-Libro [0] Cancelar\n -> '))

                while (tipoOp1 in (1,2,0)) is False: #Si la opcion no es 1, 2 o 0. Que itere hasta que sea una de las tres
                    tipoOp1=int(input('Tipo invalido. [1] Libro Impreso [2] Audio-Libro [0] Cancelar\n -> '))

                if tipoOp1!= 0:
                    titOp1=input('Ingresa su titulo: ')
                    cateOp1=input('Categoria: ')
                    pbOp1=float(input('Precio Base: '))

                    if tipoOp1 == 1:
                        nomAutorOp1=input('Nombre de Autor: ')
                        fechaEdiOp1=input('Fecha de Edicion: ')
                        cpOp1=int(input('Cantidad de Paginas: '))
                        nuevaPubicacion=LibroImpreso(tit=titOp1,cate=cateOp1,precioB=pbOp1,nomAutor=nomAutorOp1,fechaEdi=fechaEdiOp1,cantPag=cpOp1)
                    else:
                        tiemRepOp1=int(input('Tiempo de Reproduccion(en minutos): '))
                        nomNarraOp1=input('Nombre del Narrador: ')
                        nuevaPubicacion=AudioLibro(tit=titOp1,cate=cateOp1,precioB=pbOp1,tiempoRep=tiemRepOp1,nomNarra=nomNarraOp1)
                    GP.agregarPublicacion(nuevaPubicacion)
            except ValueError:
                print("Error. Se esperaba un numero")
        elif opcion==2:
            try:
                indiceOp2=int(input("Ingresa el indice: "))
                GP.getTipoPublicacion(indiceOp2)
            except ValueError:
                print("Error. Se esperaba un numero")
        elif opcion==3:
            GP.mostrarCantidadPorTipo()
        elif opcion==4:
            GP.mostrarPublicaciones()
        elif opcion==5:
            GP.listarPublicacionesConIndice()
        else:
            print("Opcion Invalida!")
        opcion=menu()
