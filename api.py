from flask import Flask, jsonify
from flask_cors import CORS
from conexao.conectar import conectar_banco
import pyodbc

app = Flask(__name__)
CORS(app)  # Libera CORS para permitir requisições do front-end

# Rotas de conexão
@app.route('/ProdutosLoja', methods=['GET'])
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
    except pyodbc.Error as err:
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    app.run(debug=True)