import os
import tkinter as tk
from tkinter import simpledialog
from database import salvar_funcionario

def criar_pasta(nome, pasta_base="funcionarios"):
    if not os.path.exists(pasta_base):
        os.makedirs(pasta_base)

    pasta_funcionario = os.path.join(pasta_base, nome)

    # Se a pasta não existir, cria e salva no banco
    if not os.path.exists(pasta_funcionario):
        os.makedirs(pasta_funcionario)
        salvar_funcionario(nome, pasta_funcionario)  # <-- integra com o banco de dados

    return pasta_funcionario


def obter_nome_pessoa():
    root = tk.Tk()
    root.withdraw()
    nome = simpledialog.askstring(
        "Cadastro Facial", 
        "Digite o nome do funcionário (ou 'sair' para encerrar):"
    )
    root.destroy()
    return nome
