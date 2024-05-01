from claseGestorDeFederados import GestorDeFederados
from claseGestorDePuntajes import GestorDePuntajes

def menu():
    op:int
    op=int(input("""
                            Menú de Opciones
                [1] Ingresa estilo y edad. Mostrar datos en funcion del estilo
                [2] Mostrar datos del patinador con mejor puntaje
                [3] Listar patinadores por estilo (tendría que ser para quienes cumplen ambos estilos)
                [4] Ingresa DNI y estilo para ver las 3 valoraciones
                [0] Salir
                 -> """))
    return op
 #El item 3 no cumple lo que pide, la idea era que muestre los que tienes ambos estilos. Yo lo codifique
 # para que solo tenga un estilo.
if __name__=='__main__':
    opcion:int
    GF= GestorDeFederados()
    GF.test()
    GP= GestorDePuntajes()
    GP.test()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            GF.listarDatosPorEstilo(GP)
        elif opcion==2:
            GP.mostrarDatosMejorPuntaje(GF)
        elif opcion==3:
            GP.listarPatinadoresPorEstilo(GF)
        elif opcion==4:
            GP.mostrarValoraciones()
        else:
            print("Opcion Invalida!")
        opcion=menu()
