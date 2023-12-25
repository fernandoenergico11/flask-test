from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://tcode.up.railway.app/"}})  # Reemplaza con tu dominio

# ... (código de conexión a la base de datos)

@app.route('/', methods=['POST'])
def actualizar_estado():
    try:
        primer_numero = request.form.get('numero1')  # Cambiado a request.form ya que estás enviando datos en el formulario

        # Reemplaza la siguiente línea con tu código de conexión a la base de datos
        # with conectar_bd() as connection:

        # Ejemplo de código de conexión simulado
        connection = None  # Reemplaza con tu código real de conexión
        with connection.cursor() as cur:
            cur.execute("INSERT INTO compra_boletas (code) VALUES (%s)", (primer_numero,))
        connection.commit()
        
        return jsonify({"success": True})  # Devuelve una respuesta JSON de éxito

    except Exception as e:
        print("Error en la transacción:", str(e))
        return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    app.run(debug=True)
