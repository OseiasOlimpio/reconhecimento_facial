# 👁️‍🗨️ Reconhecimento Facial em Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
  <img src="https://img.shields.io/badge/OpenCV-Vis%C3%A3o%20Computacional-green">
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey">
</p>

<p align="center">
  🔍 Sistema de reconhecimento facial desenvolvido em Python utilizando visão computacional e banco de dados local.
</p>

---

## 📌 Sobre o Projeto

Este projeto tem como objetivo **detectar e reconhecer rostos humanos** utilizando a webcam, aplicando conceitos de **visão computacional**, **lógica de comparação** e **persistência de dados**.

É ideal para:

- 📚 Estudos em Python  
- 🧠 Aprendizado de OpenCV  
- 🔐 Protótipos de controle de acesso  
- 🧪 Experimentos com reconhecimento facial  

---

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python**
- 👁️ **OpenCV**
- 💾 **SQLite**
- 📷 **Webcam**
- 🧠 **Lógica de comparação facial**

---

## 🗂️ Estrutura do Projeto

📦 **reconhecimento_facial**

- 🚀 `main.py`  
  Arquivo principal que inicia o sistema

- 📷 `webcam.py`  
  Captura e processa o vídeo da webcam

- 🧠 `comparador.py`  
  Responsável pela comparação facial

- 💾 `database.py`  
  Gerencia o banco de dados SQLite

- 🧰 `utils.py`  
  Funções auxiliares

- 🗄️ `funcionarios.db`  
  Banco de dados local

---
🚀 Como Usar
1) 💻 Pré-requisitos

Certifique-se de ter Python instalado (versão 3.7+).
Depois, crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

2) 📦 Instalação de Dependências

Instale as bibliotecas necessárias:

```bash
pip install opencv-python
pip install sqlite3
```

Você pode precisar instalar outras bibliotecas usadas no código, ou adaptar conforme a implementação no seu repositório.

3) ▶️ Executar o Projeto

Para iniciar o sistema de reconhecimento:

```bash
python main.py
```

Isso deve ativar a webcam e começar a detecção/identificação de rostos.

Você também pode testar módulos separados como webcam.py ou comparador.py dependendo da funcionalidade que quiser experimentar.

📷 A webcam será iniciada automaticamente e o sistema começará a detectar rostos.

🧠 Funcionamento Básico

A webcam captura o vídeo em tempo real

O OpenCV detecta os rostos

O sistema compara com os dados salvos

Se reconhecido → exibe o nome

Se não reconhecido → pode ser cadastrado (dependendo da lógica)

🔧 Funcionalidades

✅ Detecção facial em tempo real
✅ Reconhecimento de usuários cadastrados
✅ Banco de dados local (SQLite)
✅ Código modular e organizado
✅ Fácil de expandir

🌱 Possíveis Melhorias Futuras

🔐 Interface gráfica (Tkinter / PyQt)

🌐 API Web (Flask / FastAPI)

🤖 Modelos mais avançados (Deep Learning)

📊 Relatórios e logs

🖥️ Dashboard administrativo

⚠️ Aviso Importante

Este projeto é destinado a fins educacionais e protótipos.
Para uso real, é essencial considerar segurança, privacidade e legislação sobre dados biométricos.

🤝 Contribuições

Contribuições são muito bem-vindas!
Sinta-se à vontade para:

Abrir uma issue

Criar um pull request

Sugerir melhorias ✨

👨‍💻 Autor

Oseias Olímpio
📌 Desenvolvedor em formação
📎 GitHub: @OseiasOlimpio

📄 Licença

Este projeto está sob a licença MIT.
Sinta-se livre para usar, estudar e modificar 📜
