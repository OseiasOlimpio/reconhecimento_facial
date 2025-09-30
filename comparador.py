import face_recognition
import cv2
import os
from tkinter import messagebox

def carregar_referencias(pasta_base="funcionarios"):
    if not os.path.exists(pasta_base):
        os.makedirs(pasta_base)
        return [], []

    encodings = []
    nomes = []
    for pessoa in os.listdir(pasta_base):
        pessoa_path = os.path.join(pasta_base, pessoa)
        if not os.path.isdir(pessoa_path):
            continue

        for arquivo in os.listdir(pessoa_path):
            # ⚠️ Filtra somente arquivos de imagem
            if not arquivo.lower().endswith((".jpg", ".jpeg", ".png")):
                continue  

            img_path = os.path.join(pessoa_path, arquivo)

            try:
                imagem = face_recognition.load_image_file(img_path)
                rosto = face_recognition.face_encodings(imagem)
                if rosto:
                    encodings.append(rosto[0])
                    nomes.append(pessoa)
            except Exception as e:
                print(f"⚠️ Erro ao processar {img_path}: {e}")

    return encodings, nomes


def reconhecer_pessoa(pasta_base="funcionarios"):
    encodings, nomes = carregar_referencias(pasta_base)

    if not encodings:
        messagebox.showwarning("Aviso", "⚠️ Nenhum funcionário cadastrado. Cadastre um funcionário primeiro.")
   