import sqlite3
import os
from datetime import datetime

db_path = "funcionarios.db"

def inicializar_banco():
    """Cria banco de dados e tabela caso não exista"""
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            pasta TEXT NOT NULL,
            data_cadastro TEXT NOT NULL
        )
    """)
    
    conexao.commit()
    conexao.close()


def salvar_funcionario(nome, pasta):
    """Salvar funcionario no banco de dados"""
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    
    data = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    cursor.execute(
        "INSERT INTO funcionarios(nome, pasta, data_cadastro) VALUES (?, ?, ?)",  
        (nome, pasta, data)
    )
    
    conexao.commit()
    conexao.close()
  

def lista_usuario():
    """Lista todos os funcionarios cadastrados"""
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    
    conexao.close()
    return funcionarios
