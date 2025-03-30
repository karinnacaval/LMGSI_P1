from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

# Inicialització de FastAPI
app = FastAPI()

# Fitxer JSON que emmagatzema la informació dels alumnes
nom_fitxer = "alumnes.json"

# Classe per modelar les dades d'un alumne


class Alumne(BaseModel):
    nom: str
    cognom: str
    data: dict  # Diccionari amb dia, mes i any
    email: str
    feina: bool
    curs: str

# Funció per carregar els alumnes des del fitxer JSON


def carregar_alumnes():
    if os.path.exists(nom_fitxer):
        with open(nom_fitxer, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# Funció per desar els alumnes al fitxer JSON


def desar_alumnes(alumnes):
    with open(nom_fitxer, "w", encoding="utf-8") as file:
        json.dump(alumnes, file, indent=4)

# Ruta principal


@app.get("/")
def llegir_institut():
    return "Institut TIC de Barcelona"

# Ruta per obtenir el número total d'alumnes


@app.get("/alumnes/")
def obtenir_total_alumnes():
    alumnes = carregar_alumnes()
    return {"total_alumnes": len(alumnes)}

# Ruta per obtenir un alumne per ID


@app.get("/id/{id_alumne}")
def obtenir_alumne(id_alumne: int):
    alumnes = carregar_alumnes()
    alumne = next((a for a in alumnes if a["id"] == id_alumne), None)
    if alumne is None:
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    return alumne

# Ruta per esborrar un alumne per ID


@app.delete("/del/{id_alumne}")
def esborrar_alumne(id_alumne: int):
    alumnes = carregar_alumnes()
    alumnes_nous = [a for a in alumnes if a["id"] != id_alumne]
    if len(alumnes) == len(alumnes_nous):
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    # Desa la nova llista d'alumnes sense l'eliminat
    desar_alumnes(alumnes_nous)
    return {"message": "Alumne eliminat correctament"}

# Ruta per afegir un alumne


@app.post("/alumne/")
def afegir_alumne(alumne: Alumne):
    alumnes = carregar_alumnes()
    # Genera un nou ID per l'alumne
    id_nou = max((a["id"] for a in alumnes), default=0) + 1
    # Afegeix les dades de l'alumne amb l'ID generat
    alumne_dict = alumne.dict()
    alumne_dict["id"] = id_nou
    alumnes.append(alumne_dict)
    desar_alumnes(alumnes)
    return {"message": "Alumne afegit correctament", "id": id_nou}
