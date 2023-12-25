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
        db='bgumgxsdvc4biuaqa7lz',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/', methods=['POST'])
def actualizar_estado():
    try:
        numero1 = request.form.get('numero1')
        
        # Dividir la cadena en partes utilizando la coma como separador
        numeros = [num.strip() for num in numero1.split(',')]
        
        with conectar_bd() as miConexion:
            with miConexion.cursor() as cur:
                # Insertar números en la tabla compra_boletas
                cur.execute("INSERT INTO compra_boletas (code) VALUES (%s)", (numero1,))

                # Actualizar estado en la tabla grupo
                for num in numeros:
                    cur.execute("UPDATE grupo SET estado = 0 WHERE code = %s", (num,))

            miConexion.commit()

            return jsonify({"mensaje": "Estado actualizado exitosamente"})

    except ValueError:
        return jsonify({"error": "Los números proporcionados no son válidos"})
    except Exception as e:
        return jsonify({"error": f"Error desconocido: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
