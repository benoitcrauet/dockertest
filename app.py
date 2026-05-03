#!/usr/bin/env python3
from flask import Flask, request
from datetime import datetime
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def hello():
    nom = os.getenv("NOM", "Inconnu")
    return f"Bonjour {nom} c'est la V2 !\n\nDate et heure actuelle : {datetime.now().strftime('%H:%M:%S')}"

@app.route("/ascii")
def generate_figlet():
    text_to_render = request.args.get("text", "Hello")

    try:
        result = subprocess.check_output(["figlet", text_to_render], text=True)
        return f"<pre>{result}</pre>"

    except Exception as e:
        return f"Erreur lors de la génération : {str(e)}"

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
