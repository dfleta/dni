import random
from src.tablaAsignacion import TablaAsignacion
from src.cli_colors import Colors
from src.dni_cif import Dni


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

letrasNoPermitidas = ["I", "Ñ", "O", "U"]
for letraNoPermitida in letrasNoPermitidas:
    print(f"Letra {letraNoPermitida}: \
          {tabla.isLetraPermitida(letraNoPermitida)}")

### Añado casos test INCORRECTOS ALEATORIOS ###

casos_test_letra_prohibida = []
NUMERO_CASOS = 15

for i in range(1, NUMERO_CASOS + 1):
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
    # en la ultima posicion añado una letra NO PERMITIDA
    # ['I', 'Ñ', 'O', 'U']
    caso = caso + letrasNoPermitidas[random.randrange(0, 3 + 1, 1)]
    casos_test_letra_prohibida = casos_test_letra_prohibida + [caso]

print("\n## CASOS TEST LETRA NO PERMITIDA ##\n")

print(casos_test_letra_prohibida)

for dni in casos_test_letra_prohibida:
    if tabla.calcularLetra(dni[:-1]) == dni[-1]:
        print(f"{dni} {Colors.OKGREEN.value} OK {Colors.ENDC.value}")
    else:
        # print("%s %s" % (dni, Colors.FAIL + "FAIL" + Colors.ENDC))
        print(f"{dni} {Colors.FAIL.value} FAIL {Colors.ENDC.value}")


### DNI ###

print("\n\n######     DNI     ######\n")

def prettyFormatter(condition, message):
    print(f"{Colors.OKGREEN.value} {message} {Colors.ENDC.value}"
            if condition
            else f"{Colors.FAIL.value} {message} {Colors.ENDC.value}")

### Casos test DNI ALEATORIOS ###

casos_test = []
NUMERO_CASOS = 25

for i in range(1, NUMERO_CASOS + 1):
    caso = ""
    for j in range(1, 9):
        # random.randrange(start, stop[, step])
        # numeroAleatorio = random.randint(0, 9)
        # ASCII 48-57 = 0-9    65-90 = A-Z   58 = ":"
        # generamos un numero aleatorio entre 48 y 58
        caracterAscii = random.randrange(48, 58 + 1, 1)
        # convertimos el numero ASCII a caracter.
        # chr() toma el argumento como codigo ASCII de un caracter
        caso = caso + chr(caracterAscii)
    # en la ultima posicion añado una letra A-Z
    caso = caso + chr(random.randrange(65, 90 + 1, 1))
    casos_test = casos_test + [caso]

print("\n## CASOS TEST DNI ALEATORIOS ##\n")

print(casos_test)

for testString in casos_test:
    dni = Dni(testString)
    print(dni.getDni())
    dni.checkCIF()
    # print("dni --->", dni.getNumeroSano())
    # print("Letra --->", dni.getLetraSana())
    # print("La letra es", dni.obtenerLetra())
    prettyFormatter(dni.getNumeroSano(), dni.getDni())
    prettyFormatter(dni.getLetraSana(), dni.obtenerLetra())

### Casos test OK ###

CASOS_TEST_OK = [  # casos OK
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

for testString in CASOS_TEST_OK:
    dni = Dni(testString)
    print(dni.getDni())
    dni.checkCIF()
    # print("dni --->", dni.getNumeroSano())
    # print("Letra --->", dni.getLetraSana())
    # print("La letra es", dni.obtenerLetra())
    prettyFormatter(dni.getNumeroSano(), dni.getDni())
    prettyFormatter(dni.getLetraSana(), dni.obtenerLetra())
