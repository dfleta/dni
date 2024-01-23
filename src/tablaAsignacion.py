from class_bcolors_enum import Colors


class TablaAsignacion:

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

    def calcularLetra(self, DNI):
        # Obtener el numero del dni del string => dni sano
        # Dividirlo por el número de letras (actualmente 23)
        # y obtener el resto (división módulo)
        # Consultar TablaAsignacion con ese resto = posicion
        posicion = int(DNI) % self.getModulo()
        return self.getLetra(posicion)

    def __repr__(self) -> str:
        return "\n".join(self.getTabla())


if __name__ == "__main__":

    import random

    tabla = TablaAsignacion()

    print("\n## TABLA ##\n")

    # tabla.mostrarTabla()
    print(tabla)

    print("\n## ACCESO POR POSICION ##\n")

    print(tabla.getLetra(0))  # T
    print(tabla.getLetra(22)) # E
    print(tabla.getLetra(30)) # Excepcion!

    print("\n## LETRAS NO PERMITIDAS ##\n")

    letrasNoPermitidas = ["I", "Ñ", "O", "U"]
    for letra in letrasNoPermitidas:
        print(f"Letra {letra}: {tabla.isLetraPermitida(letra)}")

    casosTest = [  # casos test OK
        "78484464T",
        "72376173A",
        "01817200Q",
        "95882054E",
        "63587725Q",
        "26861694V",
        "21616083Q",
        "26868974Y",
        "40135330P",
        "89044648X",
        "80117501Z",
        "34168723S",
        "76857238R",
        "66714505S",
        "66499420A",
    ]

    ### Añado casos test FAIL ALEATORIOS ###

    numeroCasos = 15

    for i in range(1, numeroCasos + 1):
        caso = ""
        for j in range(1, 9):
            # random.randrange(start, stop[, step])
            # numeroAleatorio = random.randint(0, 9)
            # ASCII 48-57 = 0-9
            # generamos un numero aleatorio entre 48 y 57
            caracterAscii = random.randrange(48, 57 + 1, 1)
            # convertimos el numero ASCII a caracter.
            # chr() toma el argumento como codigo ASCII de un caracter
            caso = caso + chr(caracterAscii)
        # en la ultima posicion añado una letra NO PERMITIDA ['I', 'Ñ', 'O', 'U']
        caso = caso + letrasNoPermitidas[random.randrange(0, 3 + 1, 1)]
        casosTest = casosTest + [caso]

    print("\n## CASOS TEST ##\n")

    print(casosTest)

    for dni in casosTest:
        if tabla.calcularLetra(dni[:-1]) == dni[-1]:
            print(f"{dni} {Colors.OKGREEN} OK {Colors.ENDC}")
        else:
            # print("%s %s" % (dni, Colors.FAIL + "FAIL" + Colors.ENDC))
            print(f"{dni} {Colors.FAIL} FAIL {Colors.ENDC}")
