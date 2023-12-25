from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

DB_HOST = 'bgumgxsdvc4biuaqa7lz-mysql.services.clever-cloud.com'
DB_USER = 'un7kcgf6ih5t59l7'
DB_PASSWORD = 'RaJQ617Jy7Nc9gcXvE90'
DB_NAME = 'bgumgxsdvc4biuaqa7lz'

def conectar_bd():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/', methods=['POST'])
def actualizar_estado():
    try:
        # Cambié la forma de obtener el número desde los datos del formulario
        numeros = request.form.get('numero')

        with conectar_bd() as connection:
            with connection.cursor() as cur:
                cur.execute("UPDATE grupo SET estado = 0 WHERE code = %s", (numeros,))
            connection.commit()

        return jsonify({"mensaje": "Estado actualizado exitosamente"})

    except (ValueError, pymysql.Error) as error:
        return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
