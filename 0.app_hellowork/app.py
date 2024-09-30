"""Ejercicio1: crea una aplicacion web basica con flask que al ser ejecutada, inicia un servidor local en el puerto 5000.
   cuando visita la ruta principal (http://localhost:5000/), el servidor respondera con un mensaje HTML que dice "hello,word flask".
"""

# se importa el modulo Flask desde el paquete flask

from flask import Flask

#crea una instancia de la clase flask
#El argumento __name__ le dice a flask
#que utilice el nombre del archivo actual main.py

app = Flask(__name__)

#Este es un decorador que define una ruta
# corresponde a la pagina principal de la app

@app.route("/")

#cuando alguien visite la app (por ejemplo,http://localhost:5000/),
# la funcion hello() sera ejecutada

def hello():
    return "<h1> Hello, World Flask ! </h1>"

#solo se ejecuta si el archivo es ejecutado directamente
#arranca la aplicacion Flask en modo de depuracion (debug=true)

if __name__ == '__main__':
    app.run(debug=True, port=5000)