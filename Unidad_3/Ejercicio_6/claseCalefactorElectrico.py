""""Ejercicio 6 / Unidad 3 - Ary Toro"""
from claseCalefactor import Calefactor

class CalefactorElectrico(Calefactor):
    __potenciaMax:int

    def __init__(self,**kwars):
        super().__init__(kwars['Marca'],kwars['Modelo'],kwars['PaisF'],kwars['Precio'],kwars['FPago'],kwars['CCuotas'],kwars['Promo'])
        self.__potenciaMax=kwars['PotenciaM']

    def getPotenciaMax(self):
        return self.__potenciaMax

    def getImporteVenta(self):
        precioLista=self.getPrecio()
        importe=self.getPrecio()

        if self.getPromocion()=='si':
            importe-= (15*precioLista)/100

        if self.getPotenciaMax()>1000:
            importe+= (1*precioLista)/100

        if self.getFormaPago()=='cuotas':
            importe+= (30*precioLista)/100

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
                PotenciaM=self.getPotenciaMax()
                )
            )
        return d
