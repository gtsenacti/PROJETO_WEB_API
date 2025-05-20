# PROJETO_WEB_API
Repositório destinado ao projeto web, API em python. Para fins educacionais.

Executar a API antes do front (interface);

- Como rodar a API, para SQL -

No terminal da API, execute (caso os pacotes não estejam instalados):
pip install flask pyodbc flask-cors
ou este comando pip install pyodbc

Execute:
python app.py (ou pelo modo de depuração, colocando
o break point: ctrl+shift+p, Python: Select Interpreter)


- PARA MODIFICAR A API PARA RECEBER DB MYSQL -

Copiar e colar o código abaixo nos devidos arquivos:

- api.py -

from flask import Flask, jsonify
from flask_cors import CORS
from conexao.conectar import conectar_banco
import mysql.connector  # substitui pyodbc

app = Flask(__name__)
CORS(app)

@app.route('/railway', methods=['GET'])
def get_produtos():
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT produto, preco FROM produtosValores")
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()

        produtos = [{"produto": row[0], "preco": float(row[1])} for row in resultados]
        return jsonify(produtos)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    app.run(debug=True)
	
- conectar.py -

import mysql.connector

def conectar_banco():
    conexao = mysql.connector.connect(
        host="metro.proxy.rlwy.net",
        port=51260,
        user="root",
        password="SZoJhOtuAdFpahBcgQEQhRMdeJkKDsFb",
        database="railway"
    )
    return conexao


No terminal da API, execute (caso os pacotes não estejam instalados):
pip install flask mysql-connector-python flask-cors
	
Execute:
python app.py (ou pelo modo de depuração, colocando
o break point: ctrl+shift+p, Python: Select Interpreter)
