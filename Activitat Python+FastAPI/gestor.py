### Imports ##################################################
import os   # Per netejar la pantalla
import json  # Per gestionar el fitxer JSON

# Variables ###################################################

# Nom del fitxer on desar/carregar dades
nom_fitxer = "alumnes.json"
alumnes = None
### Funcions per gestionar el fitxer JSON #####################

# Carrega els alumnes des del fitxer JSON si existeix


def carregar_alumnes():
    if os.path.exists(nom_fitxer):  # Si el fitxer existeix
        fitxer = None
        with open(nom_fitxer, "r", encoding="utf-8") as file:  # Obre el fitxer en mode lectura
            # Carrega el contingut JSON com una llista
            fitxer = json.load(file)
        print(f"Fitxer llegit correctament!")
        return fitxer
    print("El fitxer no existeix, se'n crearà un de nou.")
    return []  # Si no existeix el fitxer, retorna una llista buida
# Desa els alumnes al fitxer JSON


def desar_alumnes():
    if (not alumnes):
        print("Primer has de llegir el fitxer.")
        return
    with open(nom_fitxer, "w", encoding="utf-8") as file:  # Obre el fitxer en mode escriptura
        # Desa la llista d'alumnes al fitxer JSON amb un format llegible
        json.dump(alumnes, file, indent=4)
    print("Fitxer desat.")

# Mostra tots els alumnes (id, nom, cognom)


def mostrar_alumnes():
    if not alumnes:  # Si no hi ha alumnes registrats
        print("No hi ha alumnes registrats.")
    else:
        print("ID | Nom | Cognom")  # Títols de les columnes
        print("---------------------")
        for alumne in alumnes:  # Per cada alumne a la llista
            # Mostra l'ID, nom i cognom
            print(f"{alumne['id']} | {alumne['nom']} | {alumne['cognom']}")

# Afegeix un nou alumne amb id incremental


def afegir_alumne():
    if (not alumnes):
        print("\nPrimer has de llegir el fitxer.")
        return
    # Genera un nou ID incrementant el màxim ID existent (si no hi ha cap alumne, el valor per defecte és 0)
    id_nou = max((a["id"] for a in alumnes), default=0) + 1
    nom = input("Nom: ")  # Demana el nom
    cognom = input("Cognom: ")  # Demana el cognom
    dia = int(input("Dia de naixement: "))  # Demana el dia de naixement
    mes = int(input("Mes de naixement: "))  # Demana el mes de naixement
    any = int(input("Any de naixement: "))  # Demana l'any de naixement
    email = input("Email: ")  # Demana l'email
    # Demana si l'alumne treballa (convertint a "si" o "no")
    feina = input("Treballa? (si/no): ").lower() == "si"
    curs = input("Curs: ")  # Demana el curs

    # Crea un diccionari amb la informació de l'alumne
    alumne = {
        "id": id_nou,
        "nom": nom,
        "cognom": cognom,
        # Diccionari per la data de naixement
        "data": {"dia": dia, "mes": mes, "any": any},
        "email": email,
        "feina": feina,
        "curs": curs
    }

    alumnes.append(alumne)  # Afegeix l'alumne a la llista
    # Missatge de confirmació
    print(f"\nAlumne (ID={id_nou}) afegit correctament!")
    input()

# Veure detall d'un alumne1


def veure_alumne():
    if (not alumnes):
        print("\nPrimer has de llegir el fitxer.")
        return
    id_alumne = input("Id alumne: ")

    # Busca l'alumne per ID
    # Find the first student in the list whose ID matches the given ID
    alumne = None
    for alu in alumnes:
        if int(alu["id"]) == int(id_alumne):
            alumne = alu
            break
    if alumne:  # Si l'alumne és trobat
        print(f"Nom: {alumne['nom']}")  # Mostra el nom
        print(f"Cognom: {alumne['cognom']}")  # Mostra el cognom
        # Mostra la data de naixement
        print(
            f"Data de naixement: {alumne['data']['dia']}/{alumne['data']['mes']}/{alumne['data']['any']}")
        # Mostra l'email
        print(f"Email: {alumne['email']}")
        # Mostra la feina
        print(f"Treballa? (si/no): {'si' if alumne['feina'] else 'no'}")
        print(f"Curs: {alumne['curs']}")  # Mostra el curs
    else:
        # Si l'alumne no es troba, mostra un missatge d'
        print("\nAlumne no trobat.")


def esborrar_alumne():
    global alumnes
    if (not alumnes):
        print("\nPrimer has de llegir el fitxer.")
        return
    id_alumne = input("Id alumne: ")
    alumnes_nous = [a for a in alumnes if int(a["id"]) != int(id_alumne)]
    if len(alumnes) == len(alumnes_nous):
        print("Alumne no trobat.")
    else:
        print("Alumne esborrat.")
        alumnes = alumnes_nous

### menu() ###################################################
#   Aquesta funció mostra el menú d'opcions per pantalla.
#
#   Retorna (str): l'opció escollida per l'usuari
##############################################################


def menu():
    # Netejem la pantalla
    os.system('cls')

    # Mostrem les diferents opcions
    print("Gestió alumnes")
    print("-------------------------------")
    print("1. Mostrar alumnes")
    print("2. Afegir alumne")
    print("3. Veure alumne")
    print("4. Esborrar alumne")

    print("\n5. Desar a fitxer")
    print("6. Llegir fitxer")

    print("\n0. Sortir\n\n\n")
    print(">", end=" ")

    # i retornem l'opció escollida per l'usuari
    return input()


### Programa ################################################

# Fins a l'infinit (i més enllà)
while True:

    # Executem una opció funció del que hagi escollit l'usuari
    match menu():

        # Mostrar alumnes ##################################
        case "1":
            os.system('cls')
            print("Mostrar alumnes")
            print("-------------------------------")

            # Introduiu el vostre codi per mostrar alumnes aquí

            mostrar_alumnes()
            print("\nPremeu una tecla per tornar.")
            input()
        # Afegir alumne ##################################
        case "2":
            os.system('cls')
            print("Afegir alumne")
            print("-------------------------------")

            # Introduiu el vostre codi per afegir un alumne aquí

            afegir_alumne()
            print("\nPremeu una tecla per tornar.")
            input()

        # Veure alumne ##################################
        case "3":
            os.system('cls')
            print("Veure alumne")
            print("-------------------------------")

            # Introduiu el vostre1 codi per veure un alumne aquí
            veure_alumne()
            print("\nPremeu una tecla per tornar.")
            input()

        # Esborrar alumne ##################################
        case "4":
            os.system('cls')
            print("Esborrar alumne")
            print("-------------------------------")

            # Introduiu el vostre codi per esborrar un alumne aquí
            esborrar_alumne()

            print("\nPremeu una tecla per tornar.")
            input()

        # Desar a fitxer ##################################
        case "5":
            os.system('cls')
            print("Desar a fitxer")
            print("-------------------------------")

            # Introduiu el vostre codi per desar a fitxer aquí
            desar_alumnes()
            print("\nPremeu una tecla per tornar.")
            input()

        # Llegir fitxer ##################################
        case "6":
            os.system('cls')
            print("Llegir fitxer")
            print("-------------------------------")

            # Introduiu el vostre codi per llegir de fitxer aquí

            alumnes = carregar_alumnes()

            print("\nPremeu una tecla per tornar.")
            input()

        # Sortir ##################################
        case "0":
            os.system('cls')
            print("Adeu!")

            # Trenquem el bucle infinit
            break

        # Qualsevol altra cosa #####################
        case _:
            print("\nOpció incorrecta\a")
            print("\nPremeu una tecla per tornar.")
            input()
