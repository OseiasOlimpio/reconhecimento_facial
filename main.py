import tkinter as tk
from tkinter import messagebox
from webcam import iniciar_webcam
from utils import obter_nome_pessoa, criar_pasta
from database import salvar_funcionario
from comparador import reconhecer_pessoa
from database import inicializar_banco


def cadastrar_funcionario():
  nome = obter_nome_pessoa()
  if not nome:
    messagebox.showwarning("Aviso", "⚠️ Nenhum nome fornecido, insira um nome para continuar.")
    return
  if nome.lower() == "sair":
    return
  
  pasta = criar_pasta(nome)
  salvar_funcionario(nome, pasta)
  iniciar_webcam(pasta)
  messagebox.showinfo("Sucesso", f"✅ Funcionário '{nome}' cadastrado com sucesso!")
  

inicializar_banco()

def iniciar_reconhecimento():
  reconhecer_pessoa()


def menu_gui():
  root = tk.Tk()
  root.title("Reconhecimento Facial")
  root.geometry("400x250")
  
  tk.Label(root, text= "📸Reconhecimento Facial", font=("Montserrat", 15, "bold")).pack(pady=15)
  
  tk.Button(root, text="Cadastrar funcionário", command=cadastrar_funcionario, width=25, height=2).pack(pady=5)
  tk.Button(root, text="Reconhecer funcionario", command=iniciar_reconhecimento, width=25, height=2).pack(pady=5)
  tk.Button(root, text="Sair", command=root.quit, width=25, height=2).pack(pady=5)
  
  
  root.mainloop()
  
if __name__ == "__main__":
  inicializar_banco()
  menu_gui()