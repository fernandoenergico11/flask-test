from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# Utiliza variables de entorno para almacenar información sensible como credenciales de base de datos
# Evita hardcodear estos valores directamente en el código
DB_HOST = 'bgumgxsdvc4biuaqa7lz-mysql.services.clever-cloud.com'
DB_USER = 'un7kcgf6ih5t59l7'
DB_PASSWORD = 'RaJQ617Jy7Nc9gcXvE90'
DB_NAME = 'bgumgxsdvc4biuaqa7lz'

def conectar_bd():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME
    )

@app.route('/', methods=['POST'])
def actualizar_estado():
    try:
        # En lugar de 'numeros', parece que estás recibiendo un solo número. Cambia el nombre de la variable para reflejar esto.
        numero = request.form.get('numeros')

        with conectar_bd() as miConexion:
            cur = miConexion.cursor()

            # Utiliza parámetros en la consulta para evitar SQL injection
            cur.execute("INSERT INTO compra_boletas (code) VALUES (%s)", (numero,))
            cur.execute("UPDATE grupo SET estado = 0 WHERE code IN (%s, %s)", (numero[0], numero[1]))

            miConexion.commit()

            return jsonify({"mensaje": "Estado actualizado exitosamente"})

    except ValueError:
        return jsonify({"error": "El número proporcionado no es válido"})
    except Exception as e:
        return jsonify({"error": f"Error desconocido: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
