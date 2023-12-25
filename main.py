from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# ... (código de conexión a la base de datos)
@app.route('/', methods=['POST'])
def actualizar_estado():
    try:
        primer_numero = request.json.get('numero1')  # Actualizado para coincidir con el JSON del lado del cliente
        segundo_numero = request.json.get('numero2')  # Actualizado para coincidir con el JSON del lado del cliente

        with conectar_bd() as connection:
            with connection.cursor() as cur:

                cur.execute("INSERT INTO compra_boletas (code) VALUES (%s)", (primer_numero,))
                cur.execute("INSERT INTO compra_boletas (code) VALUES (%s)", (segundo_numero,))
                
                cur.execute("UPDATE grupo SET estado = 0 WHERE code = %s", (primer_numero,))
                cur.execute("UPDATE grupo SET estado = 0 WHERE code = %s", (segundo_numero,))

            connection.commit()

        return jsonify({"mensaje": "Estado actualizado exitosamente"})

    except (ValueError, pymysql.Error) as error:
        return jsonify({"error": str(error)}), 400

    except (ValueError, pymysql.Error) as error:
    print("Error:", str(error))
    return jsonify({"error": str(error)}), 500  # Cambiado el código de estado a 500

if __name__ == '__main__':
    app.run(debug=True)
