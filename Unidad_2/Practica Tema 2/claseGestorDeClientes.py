import csv
from claseCliente import Cliente

class GestorDeClientes:
    __listaClientes:list

    def __init__(self):
        self.__listaClientes=[]

    def agregarCliente(self,uncliente):
        self.__listaClientes.append(uncliente)

    def test(self):
        band:bool=False
        archivo=open("ClientesFarmaCiudad.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if band is False:
                band=True
            else:
                self.agregarCliente(Cliente(fila[0],fila[1],int(fila[2]),int(fila[3]),float(fila[4])))
        archivo.close()

    def obtenerPosicion_porDNI(self,dni):
        i:int=0
        band:bool=False
        posicion:int=-1
        while i<len(self.__listaClientes) and band is False:
            if self.__listaClientes[i].getDNI()==dni:
                posicion=i
                band=True
            else:
                i+=1
        return posicion

    def actualizarSaldo_conOperaciones(self,GM):
        xdni:int
        i:int=0
        xnumC:int
        ayn:str
        saldoa:float
        fecha:str
        desc:str
        imp:float
        tipo:str
        pos:int
        xdni=int(input("Ingresa el DNI del Cliente: "))
        pos=self.obtenerPosicion_porDNI(xdni)
        if pos != -1:
            xnumC=self.__listaClientes[pos].getNumCuenta()
            ayn=self.__listaClientes[pos].getApellido()+" "+self.__listaClientes[pos].getNombre()
            saldoa=self.__listaClientes[pos].getSaldo()
            print(f"""
                    Cliente: {ayn}           Numero de Cuenta: {xnumC}
                    Saldo Anterior: {saldoa}
                    Movimientos
                    Fecha           Descripcion             Importe         Tipo De Movimiento""")
            for j in range(GM._GestorDeMovimientos__cantidad):
                if GM._GestorDeMovimientos__arregloMovimientos[j].getNumCuenta()==xnumC:
                    fecha=GM._GestorDeMovimientos__arregloMovimientos[j].getFecha()
                    desc=GM._GestorDeMovimientos__arregloMovimientos[j].getDescripcion()
                    imp=GM._GestorDeMovimientos__arregloMovimientos[j].getImporte()
                    tipo=GM._GestorDeMovimientos__arregloMovimientos[j].getTipo()
                    if tipo=="C":
                        saldoa+=imp
                    elif tipo=="P":
                        saldoa-=imp
                    print(f"""
                    {fecha}        {desc}             {imp}                {tipo}""")
            print(f"""
                    Saldo Actualizado: {saldoa}""")
        else:
            print("No existe un cliente con ese DNI")

    def mostrarDatos_siNoTieneMovimientos(self,GM):
        xdni:int
        xnumC:int
        xmovimientos:bool
        xdni=int(input("Ingresa el DNI del cliente: "))
        pos=self.obtenerPosicion_porDNI(xdni)
        if pos != -1:
            xnumC=self.__listaClientes[pos].getNumCuenta()
            xmovimientos=GM.existenMovimientos_porNumCuenta(xnumC)
            if xmovimientos is False:
                print("No tuvo movimientos, su nombre y apellido es: ",self.__listaClientes[pos].getNombre()+" ",self.__listaClientes[pos].getApellido())
            else:
                print("Si tuvo movimientos")
        else:
            print("No existe una cuenta con ese DNI")
