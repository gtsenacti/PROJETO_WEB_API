# Conexão com o banco de dados
import pyodbc

def conectar_banco():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-N8EH36C\\PARTICULARSQL;"
        "DATABASE=ProdutosLoja;"
        "Trusted_Connection=yes;"
    )
    return pyodbc.connect(conn_str)