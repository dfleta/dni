from src.cli_colors import Colors

class TablaAsignacion():

    # podemos utilizar este ejercicio para sobrecarga
    # de operaciones sobre listas
    def __init__(self):
        self.tabla = [
            "T",
            "R",
            "W",
            "A",
            "G",
            "M",
            "Y",
            "F",
            "P",
            "D",
            "X",
            "B",
            "N",
            "J",
            "Z",
            "S",
            "Q",
            "V",
            "H",
            "L",
            "C",
            "K",
            "E",
        ]

    def getTabla(self):
        return self.tabla

    def getLetra(self, posicion):
        try:
            return self.tabla[posicion]
        except IndexError:
            return "Posicion letra fuera de rango"

    def getModulo(self):
        return len(self.getTabla())

    def isLetraPermitida(self, letra):
        return letra in self.getTabla()

    def calcularLetra(self, numero_dni):
        # Obtener el numero del dni del string => dni sano
        # Dividirlo por el número de letras (actualmente 23)
        # y obtener el resto (división módulo)
        # Consultar TablaAsignacion con ese resto = posicion
        posicion = int(numero_dni) % self.getModulo()
        return self.getLetra(posicion)

    def __repr__(self) -> str:
        return ' '.join(self.getTabla())
