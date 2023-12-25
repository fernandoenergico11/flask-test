from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://tcode.up.railway.app/"}})  # Reemplaza con tu dominio

# ... (código de conexión a la base de datos)
@app.route('/', methods=['POST'])
def actualizar_estado():
    try:
        primer_numero = request.json.get('numero1')  # Actualizado para coincidir con el JSON del lado del cliente

        with conectar_bd() as connection:
    try:
        with connection.cursor() as cur:
            cur.execute("INSERT INTO compra_boletas (code) VALUES (%s)", (primer_numero,))
        connection.commit()
    except pymysql.Error as e:
        connection.rollback()
        print("Error en la transacción:", str(e))
        return jsonify({"error": "Error interno del servidor"}), 500
        
if __name__ == '__main__':
    app.run(debug=True)
