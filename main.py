from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# ... (otras rutas)

@app.route('/', methods=['GET'])
def mostrar_numeros():
    cantidad_aleatorios = 2

    # Configuración de la conexión a la base de datos usando with statement
    try:
        with pymysql.connect(host='bgumgxsdvc4biuaqa7lz-mysql.services.clever-cloud.com', user='un7kcgf6ih5t59l7', passwd='RaJQ617Jy7Nc9gcXvE90', db='bgumgxsdvc4biuaqa7lz') as miConexion:
            cur = miConexion.cursor()

            # Obtener la cantidad total de registros en la tabla para los números con estado=1
            cur.execute("SELECT COUNT(*) FROM grupo WHERE estado=1")
            total_registros_estado = cur.fetchone()[0]

            # Verificar si hay suficientes registros activos para obtener la cantidad deseada
            if total_registros_estado < cantidad_aleatorios:
                return "No hay suficientes registros activos para obtener la cantidad deseada."
            else:
                # Crear la consulta SQL con los números aleatorios
                consulta_sql = f"SELECT code FROM grupo WHERE estado=1 ORDER BY RAND() LIMIT 2"
                cur.execute(consulta_sql)

                # Obtener los códigos elegidos
                elegidos = [code[0] for code in cur.fetchall()]

                if len(elegidos) == cantidad_aleatorios:
                    # Insertar los números aleatorios en la tabla "compra_boletas"
                    for num_aleatorio in elegidos:
                        cur.execute("INSERT INTO compra_boletas (code) VALUES (%s)", (num_aleatorio,))
                        # Actualizar el campo "estado" en la tabla "grupo"
                        cur.execute("UPDATE grupo SET estado = 0 WHERE code = %s", (num_aleatorio,))

                    # Confirmar la transacción y cerrar la conexión
                    miConexion.commit()

                    # Renderizar la plantilla HTML con los números aleatorios
                    return render_template('numeros.html', numeros=elegidos)
    except pymysql.Error as e:
        # Manejo de excepciones para errores de base de datos
        return f"Error de base de datos: {e}"

if __name__ == '__main__':
    app.run(debug=True)
