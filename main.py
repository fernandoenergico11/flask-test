from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

def conectar_bd():
    return pymysql.connect(
        host='bgumgxsdvc4biuaqa7lz-mysql.services.clever-cloud.com',
        user='un7kcgf6ih5t59l7',
        passwd='RaJQ617Jy7Nc9gcXvE90',
        db='bgumgxsdvc4biuaqa7lz'
    )

@app.route('/', methods=['GET'])
def actualizar_estado():
    try:

        numero1='004'
        numero2='016'

        with conectar_bd() as miConexion:
            cur = miConexion.cursor()

            # Insertar números en la tabla compra_boletas
            cur.execute("INSERT INTO compra_boletas (code) VALUES (%s)", (numero1,))
            cur.execute("INSERT INTO compra_boletas (code) VALUES (%s)", (numero2,))

            # Actualizar estado en la tabla grupo
           # Actualizar estado en la tabla grupo
            cur.execute("UPDATE grupo SET estado = 0 WHERE code IN (%s, %s)", (numero1, numero2))


            miConexion.commit()

            return jsonify({"mensaje": "Estado actualizado exitosamente"})

    except ValueError:
        return jsonify({"error": "Los números proporcionados no son válidos"})
    except Exception as e:
        return jsonify({"error": f"Error desconocido: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
