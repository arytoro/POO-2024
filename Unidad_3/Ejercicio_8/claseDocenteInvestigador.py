"""Ejercicio 7 / Unidad 3 - Ary Toro"""
from claseDocente import Docente
from claseInvestigador import Investigador

class DocenteInvestigador(Docente,Investigador):
    __cateDeIncentivo:str
    __importeExtra:float

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__cateDeIncentivo=kwargs['CateI']
        self.__importeExtra=kwargs['ImpExtra']

    def getCategoriaIncentivo(self):
        return self.__cateDeIncentivo

    def getImporteExtra(self):
        return self.__importeExtra

    def setImporteExtra(self,nuevoImp):
        self.__importeExtra=nuevoImp

    def __str__(self):
        return f"""
            °CUIL: {self.getCuil()}
             Apellido: {self.getApellido()}
             Nombre: {self.getNombre()}
             Sueldo Basico: {self.getSueldoBasico()}
             Antiguedad: {self.getAntiguedad()}
             Carrera: {self.getCarrera()}
             Cargo: {self.getCargo()}
             Catedra: {self.getCatedra()}
             Area de Investigacion: {self.getArea()}
             Tipo de Investigacion: {self.getTipo()}
             Categoria en el Programa de Incentivos: {self.getCategoriaIncentivo()}
             Importe Extra: {self.getImporteExtra()}"""

    def getSueldoTotal(self):
        return super().getSueldoTotal()+self.getImporteExtra()

    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                Cuil=self.getCuil(),
                Ape=self.getApellido(),
                Nom=self.getNombre(),
                SueldoB=self.getSueldoBasico(),
                Antig=self.getAntiguedad(),
                Carrera=self.getCarrera(),
                Cargo=self.getCargo(),
                Catedra=self.getCatedra(),
                PorcCargo=self.getPorcentajePCargo(),
                Area=self.getArea(),
                Tipo=self.getTipo(),
                CateI=self.getCategoriaIncentivo(),
                ImpExtra=self.getImporteExtra(),
                )
            )
        return d
