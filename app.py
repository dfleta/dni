import random
from src.tablaAsignacion import TablaAsignacion
from src.cli_colors import Colors
from src.dni_cif import Dni

LETRAS_NO_PERMITIDAS = ["I", "Ñ", "O", "U"]


def mostrarLetrasNoPermitidas(tabla):
    for letra_no_permitida in LETRAS_NO_PERMITIDAS:
        print(f"Letra {letra_no_permitida}: {tabla.isLetraPermitida(letra_no_permitida)}")


def generarDNIaleatorio():
    CERO_ASCII = 48
    NUEVE_ASCII = 57
    LONGITUD_DNI = 8
    # DNI tiene 8 digitos
    # ASCII 48-57 = 0-9
    # generamos un numero aleatorio entre 48 y 57
    # convertimos el numero ASCII a caracter.
    # chr() toma el argumento como codigo ASCII de un caracter
    return ''.join([chr(random.randrange(CERO_ASCII, NUEVE_ASCII + 1))
                   for _ in range(LONGITUD_DNI)])


def generarCIFsLetraNoPermitida(numero_casos):
    # en la ultima posicion añado una letra NO PERMITIDA
    # ['I', 'Ñ', 'O', 'U']
    return [generarDNIaleatorio()
            + LETRAS_NO_PERMITIDAS[random.randrange(0, \
                                   len(LETRAS_NO_PERMITIDAS))]
            for _ in range(numero_casos)]


def generarCIFsAleatorios(numero_casos):
    A_ASCII = 65
    Z_ASCII = 90
    # en la ultima posicion añado una letra A-Z
    # ASCII 65-90 = A-Z
    return [generarDNIaleatorio()
            + chr(random.randrange(A_ASCII, Z_ASCII + 1))
            for _ in range(numero_casos)]


def generarCIFsAleatoriosMalFormados(numero_casos):
    DOS_PUNTOS_ASCII = 58
    cifs_aleatorios = []
    for _ in range(numero_casos):
        cif = list(generarCIFsAleatorios(1)[0])
        posicion = random.randint(0, len(cif[:-1]) - 1)
        cif[posicion] = chr(DOS_PUNTOS_ASCII)
        cifs_aleatorios.append(''.join(cif))
    return cifs_aleatorios


def prettyFormatter(condition, message):
    color = Colors.OKGREEN.value if condition else Colors.FAIL.value
    return f"{color} {message} {Colors.ENDC.value}"


def main():

    ### TABLA ASIGNACION ###

    tabla = TablaAsignacion()

    print("\n######     TABLA     ######\n")

    print(tabla)

    print("\n## ACCESO POR POSICION ##\n")

    print(tabla.getLetra(0))  # T
    print(tabla.getLetra(22)) # E
    print(tabla.getLetra(30)) # Excepcion!

    print("\n## LETRAS NO PERMITIDAS ##\n")

    mostrarLetrasNoPermitidas(tabla)

    ### Añado casos test INCORRECTOS ALEATORIOS ###

    numero_casos = 15
    cifs_letra_no_permitida = generarCIFsLetraNoPermitida(numero_casos)

    print("\n## CASOS TEST LETRA NO PERMITIDA ##\n")

    for cif in cifs_letra_no_permitida:
        print(prettyFormatter(tabla.calcularLetra(cif[:-1]) == cif[-1], cif))

    ### DNI ###

    print("\n\n######     DNI     ######\n")

    ### Casos test DNI ALEATORIOS ###

    numero_casos = 15
    cifs_aleatorios = generarCIFsAleatorios(numero_casos)

    print("\n## CASOS TEST DNI ALEATORIOS ##\n")

    for cif in cifs_aleatorios:
        dni = Dni(cif)
        dni.checkCIF()
        print(prettyFormatter(dni.getNumeroSano(), dni.getDni()))
        print(prettyFormatter(dni.getLetraSana(), dni.obtenerLetra()))

    print("\n## CASOS TEST DNI ALEATORIOS MAL FORMADOS ##\n")

    cifs_aleatorios = generarCIFsAleatoriosMalFormados(numero_casos)

    for cif in cifs_aleatorios:
        dni = Dni(cif)
        dni.checkCIF()
        print(prettyFormatter(dni.getNumeroSano(), dni.getDni()))
        print(prettyFormatter(dni.getLetraSana(), dni.obtenerLetra()))

    ### Casos test OK ###

    cifs_ok = [  # casos OK
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

    print("\n #### CASOS TEST DNI OK #### \n")

    for cif_ok in cifs_ok:
        dni = Dni(cif_ok)
        dni.checkCIF()
        print(prettyFormatter(dni.getNumeroSano(), dni.getDni()))
        print(prettyFormatter(dni.getLetraSana(), dni.obtenerLetra()))


if __name__ == "__main__":
    # Esta estructura de app y main permite:
    # - Importar el módulo sin efectos secundarios:
    #       no se ejecuta el codigo al importar el modulo.
    # - Existe un punto de entrada claro a la aplicación.
    # - Permite el testing.
    # - Separa el código del script del código del módulo.
    main()
