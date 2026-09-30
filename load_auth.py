import json
import imaplib

def donnes_connexions() :
    with open(".connexion.json", "r", encoding="utf-8") as f:
        credentials = json.load(f)

        email = credentials["email"]
        password = credentials["password"]
    return (email,password)    