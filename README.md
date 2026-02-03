👁️‍🗨️ Reconhecimento Facial em Python
<p align="center"> <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python"> <img src="https://img.shields.io/badge/OpenCV-Vis%C3%A3o%20Computacional-green"> <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow"> <img src="https://img.shields.io/badge/License-MIT-lightgrey"> </p> <p align="center"> 🔍 Sistema de reconhecimento facial desenvolvido em Python utilizando visão computacional e banco de dados local. </p>

📌 Sobre o Projeto

Este projeto tem como objetivo detectar e reconhecer rostos humanos utilizando a webcam, aplicando conceitos de visão computacional, lógica de comparação e persistência de dados.

É ideal para:

📚 Estudos em Python

🧠 Aprendizado de OpenCV

🔐 Protótipos de controle de acesso

🧪 Experimentos com reconhecimento facial

🛠️ Tecnologias Utilizadas

🐍 Python

👁️ OpenCV

💾 SQLite

📷 Webcam

🧠 Lógica de comparação facial

📂 Estrutura do Projeto
📦 reconhecimento_facial
├── comparador.py       # Lógica de comparação de rostos
├── database.py         # Conexão e manipulação do banco SQLite
├── funcionarios.db     # Banco de dados local
├── main.py             # Arquivo principal do sistema
├── utils.py            # Funções auxiliares
├── webcam.py           # Captura de vídeo e detecção facial
├── __pycache__/
└── README.md

🚀 Como Executar o Projeto
🔹 Pré-requisitos

Python 3.7 ou superior

Webcam funcional

🔹 Instalação das Dependências
pip install opencv-python


O SQLite já vem integrado com o Python.

▶️ Executar
python main.py


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
