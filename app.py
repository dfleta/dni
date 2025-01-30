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
    dni = ""
    # DNI tiene 8 digitos
    for _ in range(LONGITUD_DNI):
        # random.randrange(start, stop[, step])
        # numeroAleatorio = random.randint(0, 9)
        # ASCII 48-57 = 0-9
        # generamos un numero aleatorio entre 48 y 57
        caracter_ascii = random.randrange(CERO_ASCII, NUEVE_ASCII + 1)
        # convertimos el numero ASCII a caracter.
        # chr() toma el argumento como codigo ASCII de un caracter
        dni += chr(caracter_ascii)
    return dni


def generarCIFLetraNoPermitida(numero_casos):
    cif_con_letra_prohibida = []
    for _ in range(numero_casos):
        dni = generarDNIaleatorio()
        # en la ultima posicion añado una letra NO PERMITIDA
        # ['I', 'Ñ', 'O', 'U']
        cif = dni + LETRAS_NO_PERMITIDAS[random.randrange(0, \
                                                    len(LETRAS_NO_PERMITIDAS))]
        cif_con_letra_prohibida.append(cif)
    return cif_con_letra_prohibida


def generar_cifs_aleatorios(numero_casos):
    LONGITUD_DNI = 8
    CERO_ASCII = 48
    DOS_PUNTOS_ASCII = 58
    dnis_aleatorios = []
    for _ in range(numero_casos):
        dni = ""
        for _ in range(LONGITUD_DNI):
            # ASCII 48-57 = 0-9    65-90 = A-Z   58 = ":"
            caracter_ascii = random.randrange(CERO_ASCII, DOS_PUNTOS_ASCII + 1)
            # convertimos el numero ASCII a caracter.
            dni += chr(caracter_ascii)
        # en la ultima posicion añado una letra A-Z
        cif = dni + chr(random.randrange(65, 90 + 1, 1))
        dnis_aleatorios.append(cif)
    return dnis_aleatorios


def prettyFormatter(condition, message):
    print(f"{Colors.OKGREEN.value} {message} {Colors.ENDC.value}"
            if condition
            else f"{Colors.FAIL.value} {message} {Colors.ENDC.value}")


def main():

    ### TABLA ASIGNACION ###

    tabla = TablaAsignacion()

    print("\n######     TABLA     ######\n")

    # tabla.mostrarTabla()
    print(tabla)

    print("\n## ACCESO POR POSICION ##\n")

    print(tabla.getLetra(0))  # T
    print(tabla.getLetra(22)) # E
    print(tabla.getLetra(30)) # Excepcion!

    print("\n## LETRAS NO PERMITIDAS ##\n")

    mostrarLetrasNoPermitidas(tabla)

    ### Añado casos test INCORRECTOS ALEATORIOS ###

    numero_casos = 15
    cifs_letra_no_permitida = generarCIFLetraNoPermitida(numero_casos)

    print("\n## CASOS TEST LETRA NO PERMITIDA ##\n")

    print(cifs_letra_no_permitida)

    for cif in cifs_letra_no_permitida:
        if tabla.calcularLetra(cif[:-1]) == cif[-1]:
            print(f"{cif} {Colors.OKGREEN.value} OK {Colors.ENDC.value}")
        else:
            # print("%s %s" % (dni, Colors.FAIL + "FAIL" + Colors.ENDC))
            print(f"{cif} {Colors.FAIL.value} FAIL {Colors.ENDC.value}")


    ### DNI ###

    print("\n\n######     DNI     ######\n")

    ### Casos test DNI ALEATORIOS ###

    numero_casos = 25
    cifs_aleatorios = generar_cifs_aleatorios(numero_casos)

    print("\n## CASOS TEST DNI ALEATORIOS ##\n")

    print(cifs_aleatorios)

    for cif in cifs_aleatorios:
        dni = Dni(cif)
        print(dni.getDni())
        dni.checkCIF()
        # print("dni --->", dni.getNumeroSano())
        # print("Letra --->", dni.getLetraSana())
        # print("La letra es", dni.obtenerLetra())
        prettyFormatter(dni.getNumeroSano(), dni.getDni())
        prettyFormatter(dni.getLetraSana(), dni.obtenerLetra())

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
        print(dni.getDni())
        dni.checkCIF()
        # print("dni --->", dni.getNumeroSano())
        # print("Letra --->", dni.getLetraSana())
        # print("La letra es", dni.obtenerLetra())
        prettyFormatter(dni.getNumeroSano(), dni.getDni())
        prettyFormatter(dni.getLetraSana(), dni.obtenerLetra())



if __name__ == "__main__":
    main()
