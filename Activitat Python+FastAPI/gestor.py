### Imports ##################################################
import os   # Per netejar la pantalla
import json  # Per gestionar el fitxer JSON

# Variables ###################################################

# Nom del fitxer on desar/carregar dades
nom_fitxer = "alumnes.json"

### Funcions per gestionar el fitxer JSON #####################

# Carrega els alumnes des del fitxer JSON si existeix


def carregar_alumnes():
    if os.path.exists(nom_fitxer):  # Si el fitxer existeix
        with open(nom_fitxer, "r", encoding="utf-8") as file:  # Obre el fitxer en mode lectura
            return json.load(file)  # Carrega el contingut JSON com una llista
    return []  # Si no existeix el fitxer, retorna una llista buida

# Desa els alumnes al fitxer JSON


def desar_alumnes(alumnes):
    with open(nom_fitxer, "w", encoding="utf-8") as file:  # Obre el fitxer en mode escriptura
        # Desa la llista d'alumnes al fitxer JSON amb un format llegible
        json.dump(alumnes, file, indent=4)
    # Missatge confirmant que les dades s'han desat correctament
    print("\nDades desades correctament!")

# Mostra tots els alumnes (id, nom, cognom)


def mostrar_alumnes(alumnes):
    if not alumnes:  # Si no hi ha alumnes registrats
        print("No hi ha alumnes registrats.")
    else:
        print("ID | Nom | Cognom")  # Títols de les columnes
        print("---------------------")
        for alumne in alumnes:  # Per cada alumne a la llista
            # Mostra l'ID, nom i cognom
            print(f"{alumne['id']} | {alumne['nom']} | {alumne['cognom']}")

# Afegeix un nou alumne amb id incremental


def afegir_alumne(alumnes):
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
    print("\nAlumne afegit correctament!")  # Missatge de confirmació

# Veure detall d'un alumne


def veure_alumne(alumnes, id_alumne):
    # Busca l'alumne per ID
    alumne = next((a for a in alumnes if a["id"] == id_alumne), None)
    if alumne:  # Si l'alumne és trobat
        # Mostra la informació de l'alumne en format JSON (bé formatat)
        print(json.dumps(alumne, indent=4))
    else:
        # Si l'alumne no es troba, mostra un missatge d'
        print("\nAlumne no trobat.")
