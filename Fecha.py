class Fecha:
    __dia = int(0)
    __mes = int(0)
    __anio = int(0)
    __diasiguiente = int(0)
    __messiguiente = int(0)
    __aniosiguiente= int(0)
    def __init__(self, dia, mes, anio):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
    def verificarfecha(self):
        self.__dia = self.__dia + 1
        if (self.__dia>30):
            self.__dia = 1
            self.__mes = self.__mes + 1
            self.__diasiguiente = self.__dia
            self.__mes = self.__mes + 1
            if (self.__mes > 12):
                self.__mes = 1
                self.__messiguiente = self.__mes
                self.__anio = self.__anio + 1
                self.__aniosiguiente = self.__anio
    def getDiaSiguiente(self):
        return self.__dia
    def getMesSiguiente(self):
        return self.__mes
    def getAnioSiguiente(self):
        return self.__anio
