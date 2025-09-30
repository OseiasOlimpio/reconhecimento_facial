import cv2
import mediapipe as mp
import os
import time
from utils import obter_nome_pessoa

# Iniciando OpenCV e MediaPipe
def iniciar_webcam(nome_pessoa: str):
  pasta = os.path.join("funcionarios", nome_pessoa)
  os.makedirs(pasta, exist_ok=True)
  
  webcam = cv2.VideoCapture(0)
  if not webcam.isOpened():
      raise Exception("Não foi possível acessar a webcam")
  reconhecimento = mp.solutions.face_detection
  reconhecedor_de_rostos = reconhecimento.FaceDetection()
  desenho = mp.solutions.drawing_utils
  # Contagem regressiva de 3 segundos
  for i in range(3, 0, -1):
      ret, frame = webcam.read()
      if not ret:
          break
      # Escreve número no centro da tela
      cv2.putText(frame, str(i), (frame.shape[1]//2 - 50, frame.shape[0]//2),
                  cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), 5, cv2.LINE_AA)
      cv2.imshow("Reconhecimento Facial", cv2.flip(frame, 1))
      cv2.waitKey(1)
      time.sleep(1)  # Espera 1 segundo entre cada número
  contador = 0
  while True:
      # Captura frame da webcam
      verificador, frame = webcam.read()
      if not verificador:
          break
      # Reconhece rostos
      lista_rostos = reconhecedor_de_rostos.process(frame)
      # Desenha bounding box no rosto
      if lista_rostos.detections:
          for rosto in lista_rostos.detections:
              desenho.draw_detection(frame, rosto)
      # Mostra imagem
      cv2.imshow("Reconhecimento Facial", cv2.flip(frame, 1))
      # Se pressionar ESC ou fechar janela → encerra
      if cv2.waitKey(25) == 27:
          break
      if cv2.getWindowProperty("Reconhecimento Facial", cv2.WND_PROP_VISIBLE) < 1:
          break
      # Salva imagens na pasta do usuário
      if contador < 10:
          img_path = os.path.join(pasta, f"{nome_pessoa}_{contador}.jpg")
          cv2.imwrite(img_path, frame)
          contador += 1
          if contador == 10:
              break
            
  webcam.release()
  cv2.destroyAllWindows()