from claseLista import Lista,ClienteLocal,ClienteNacional

def menu():
    op=None
    try:
        op=int(input("""
                    Menu de Opciones
        [1] Agregar cliente al final de la lista (Ingresa manual)
        [2] Mostrar datos de Clientes Nacionales
        [3] Ingresar posicion para conocer tipo de Cliente
        [4] ADICION. Test Cargar clientes (automatico)
        [5] ADICION. Mostrar todos los datos
        [0] SALIR
        -> """))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    GC=Lista()
    opcion=menu()
    nuevoCliente=None
    while opcion!=0:
        if opcion==1:
            try:
                tipo=int(input("De que tipo?: \n [1] Nacional\n [2] Local \n [0] Cancelar \n -> "))
                if tipo in (1,2,0):
                    if tipo!=0:
                        nombre=input("°Nombre: ")
                        apellido=input(" Apellido: ")
                        email=input(" Email: ")
                        contrasenia=input(" Contrasenia: ")
                        direccionPostal=input(" Direccion Postal: ")
                        telefono=int(input(" Telefono: "))
                        if tipo==1:
                            provincia=input(" Provincia: ")
                            localidad=input(" Localdiad: ")
                            codigoPostal=int((input(" Codigo Postal: ")))
                            nuevoCliente=ClienteNacional(nombre,apellido,email,contrasenia,direccionPostal,telefono,provincia,localidad,codigoPostal)
                        elif tipo==2:
                            nuevoCliente=ClienteLocal(nombre,apellido,email,contrasenia,direccionPostal,telefono)

                        GC.agregarCliente(nuevoCliente)
                    else:
                        print("...Cancelando Operacion de Carga")
                else:
                    print("Opcion Invalida!")
            except ValueError:
                print("Error. Se esperaba un numero entero")
        elif opcion==2:
            GC.listarClientesNacionales()
        elif opcion==3:
            try:
                indice=int(input("Indice: "))
                GC.mostrarTipoCliente(indice)
            except ValueError:
                print("Error. Se esperaba un numero entero")
            except IndexError:
                print("Error. El indice no es valido")
        elif opcion==4:
            cliente1=ClienteNacional("Mario","Perez", "mp@gamil.com","ajfk832","Mendoza 182",7283,"La Rioja","Vida",6712)
            cliente2=ClienteLocal("Rocio","Luna","rc@gmail.com","73823d","Patagonia 723",9281)
            cliente3=ClienteNacional("Jorge","Sanchez","js@gmail.com","hud3uy7","Tucuman 219",9392,"San Luis","Villa Mercedes",8123)
            cliente4=ClienteNacional("Mariana","Riveros","mr@gmail.com","74yrh","San Martin 452",8217,"Buenos Aires","Capital",7291)
            GC.agregarCliente(cliente1)
            GC.agregarCliente(cliente2)
            GC.agregarCliente(cliente3)
            GC.agregarCliente(cliente4)
        elif opcion==5:
            GC.listarTodo()
        else:
            print("Opcion Invalida!")
        opcion=menu()

            
""" Lote de Prueba
1
1
Mario
Perez
mp@gamil.com
ajfk832
Mendoza 182
7283
La Rioja
Vida
6712
1
2
Rocio
Luna
rc@gmail.com
7382d3
Patagonia 723
9281
1
1
Jorge
Sanchez
js@gmail.com
hud3uy7
Tucuman 219
9392
San Luis
Villa Mercedes
8123
"""