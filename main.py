from flask import Flask, request

app = Flask(__name__)

@app.route('https://tocde.up.railway.app', methods=['POST'])
def actualizar_estado():
    numero1 = request.form.get('numero1')
    numero2 = request.form.get('numero2')

    # Realizar la actualización en la base de datos con los valores de numero1 y numero2

    return 'Estado actualizado exitosamente'

if __name__ == '__main__':
    app.run(debug=True)
