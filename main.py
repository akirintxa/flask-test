from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hola pepsicola o cocacola'


# Para ejecutar el servidor FLASK
# Opción 1: Variables de entorno
# Crear una variable de entorno export FLASK_APP=main.py
# Verificar el valor de la variable echo $FLASK_APP
# Se ejecuta en la terminal >flask run
# Opción 2: Agregar estas líneas al final de main.py
# if __name__ == "__main__":
#     app.run(port=8080)

# Para encender el modo debug
# Opción 1: Variables de entorno
# export FLASK_DEBUG=1
# Opción 2: Agregar estas líneas al final de main.py
# if __name__ == "__main__":
#     app.run(port=8080, debug = True))