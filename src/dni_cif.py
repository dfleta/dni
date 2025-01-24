from src.tablaAsignacion import TablaAsignacion


class Dni:

    def __init__(self, cadena=""):
        self.dni = cadena
        self.numeroSano = False
        self.letraSana = False
        # Composición (agregación) "Has - a" / "Tiene - un"
        self.tabla = TablaAsignacion()

    ### interfaz PUBLICA ###

    def setDni(self, cadena):
        self.dni = cadena

    def getDni(self):
        return self.dni

    def getNumeroSano(self):
        return self.numeroSano

    def getLetraSana(self):
        return self.letraSana

    def checkCIF(self):
        return self.checkDni() and self.checkLetra()

    def checkDni(self):
        self.__setNumeroSano(self.__checkLongitud() and self.__checkNumero())
        return self.getNumeroSano()

    def checkLetra(self):
        if self.getNumeroSano():
            self.__setLetraSana(
                self.getParteAlfabeticaDni().isupper()
                and not self.getParteAlfabeticaDni().isdigit()
                and self.__checkLetraValida()
            )
            return self.getLetraSana()
        else:
            return False

    def obtenerLetra(self):
        # calcularLetra no puede ejecutarse si antes
        # no se cumplen las condiciones previas
        # en checkDni y checkletra
        if self.getNumeroSano():
            return self.tabla.calcularLetra(self.getParteNumericaDni())
        else:
            return None

    ### parte PRIVADA ###

    def __setNumeroSano(self, valor):
        self.numeroSano = valor

    def __setLetraSana(self, valor):
        self.letraSana = valor

    def __checkLongitud(self):
        return len(self.getDni()) == 9

    def __checkNumero(self):
        return self.dni[:-1].isdigit()

    def __checkLetraValida(self):
        if self.getNumeroSano():
            return self.getParteAlfabeticaDni() == self.obtenerLetra()
        else:
            return False

    def getParteAlfabeticaDni(self):
        return self.dni[-1]

    def getParteNumericaDni(self):
        if self.getNumeroSano():
            return self.dni[:-1]
        else:
            return False
