from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
from contextlib import closing  # Importa la función closing para manejar mejor las conexiones

app = Flask(__name__)
CORS(app)

# Utiliza variables de entorno para almacenar información sensible como credenciales de base de datos
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
        cursorclass=pymysql.cursors.DictCursor  # Establece el tipo de cursor para obtener resultados como diccionarios
    )

@app.route('/', methods=['POST'])
def actualizar_estado():
    try:
        # Cambia la forma de obtener el número cuando se envían datos JSON
        data = request.get_json()
        numeros = data.get('numero')  # Se espera una lista de números

        if not numeros or not isinstance(numeros, list):
            raise ValueError("Se esperaba una lista de números en el campo 'numero'")

        with closing(conectar_bd()) as miConexion:
            with miConexion.cursor() as cur:
                for numero in numeros:
                    cur.execute("UPDATE grupo SET estado = 0 WHERE code = %s", (numero,))

            miConexion.commit()

            return jsonify({"mensaje": "Estado actualizado exitosamente"})

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": f"Error desconocido: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
