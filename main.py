from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# ... (código de conexión a la base de datos)

@app.route('/', methods=['POST'])
def actualizar_estado():
    try:
        numeros = request.json.get('numero')

        with conectar_bd() as connection:
            with connection.cursor() as cur:
                # Utilizando placeholders para construir la consulta de manera segura
                placeholders = ', '.join(['%s'] * len(numeros))
                query = f"UPDATE grupo SET estado = 0 WHERE code IN ({placeholders})"
                cur.execute(query, numeros)
            connection.commit()

        return jsonify({"mensaje": "Estado actualizado exitosamente"})

    except (ValueError, pymysql.Error) as error:
        return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
