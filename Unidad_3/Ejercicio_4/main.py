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
            [0] SALIR
            -> """))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    GP=Lista()
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
                        fechaEdiOp1=input('Fecha de Edicion(dd/mm/yyyy): ')
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
        else:
            print("Opcion Invalida!")
        opcion=menu()

"""Lote De Prueba para carga (presionar opcion 1 y luego pegar lo de abajo)
1
El misterio del faro
Misterio
1300
Elena Garcia
10/05/2022
280
1
2
El secreto de NY
Suspenso
750
300
Ana Martínez
1
1
Aventuras en la selva
Aventura
950
Juan Perez
23/05/2024
200
1
1
Recetas del mundo
Cocina
650
Maria Lopez
22/08/2023
350
1
2
Viaje al futuro
Ciencia Ficcion
1500
420
Pedro Fernandez
"""
