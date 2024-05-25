""""Ejercicio 6 / Unidad 3 - Ary Toro"""
from claseCalefactor import Calefactor

class CalefactorGas(Calefactor):
    __matricula:str
    __calorias:str

    def __init__(self,**kwars):
        super().__init__(kwars['Marca'],kwars['Modelo'],kwars['PaisF'],kwars['Precio'],kwars['FPago'],kwars['CCuotas'],kwars['Promo'])
        self.__matricula=kwars['Matricula']
        self.__calorias=kwars['Calorias']

    def getMatricula(self):
        return self.__matricula

    def getCalorias(self):
        return self.__calorias

    def getImporteVenta(self):
        precioLista=self.getPrecio()
        importe=self.getPrecio()

        if self.getPromocion()=='si':
            importe-= (15*precioLista)/100

        if self.getCalorias()>3000:
            importe+= (1*precioLista)/100

        if self.getFormaPago()=='cuotas':
            importe+= (40*precioLista)/100

        return importe

    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                Marca=self.getMarca(),
                Modelo=self.getModelo(),
                PaisF=self.getPaisFabrica(),
                Precio=self.getPrecio(),
                FPago=self.getFormaPago(),
                CCuotas=self.getCantCuotas(),
                Promo=self.getPromocion(),
                Matricula=self.getMatricula(),
                Calorias=self.getCalorias()
                )
            )
        return d
