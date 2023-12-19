import random
from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def mostrar_numeros():
    return render_template('numeros.html')


if __name__ == '__main__':
    app.run(debug=True)
