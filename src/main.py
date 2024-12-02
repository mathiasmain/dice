# Neste programa, iremos usar o modelo já criado para aplicá-lo em vídeos.

# Objetivos
# Para o modelo responder algo, ele precisa de uma imagem "perfeita".
# Então, talvez fosse interessante um pedaço de código que:
# 1. Saiba detectar um rosto em um frame ( imagem ).
# 2. Com uma certa margem, faz um corte no frame com o rosto do infeliz.
# 3. Modifica o tamanho para 64x64 e testa o frame no modelo.
# 4. Retorna um frame com a resposta escrita no canto da tela com CV2.

import  cv2
import  tensorflow          as      tf
from    tensorflow          import  keras
from    tensorflow.keras    import  layers, models

# Carrega o modelo para usar na função whatEmotion
model = keras.models.load_model('./dice.hdf5')

# Carrega no classificador para usar na função detect_bouding_box
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Para acessar a câmera do dispositivo, substitua ("josh.mp4") por (0).
capture = cv2.VideoCapture("josh.mp4")



while(cap.isOpened()):
    result, frame = cap.read()
    if result  is False:
        break
    
    print(frame.shape)
    
    # -------------------Aqui que faz a bagunça
    
    
    # Detect MultiScale detecta rostos de vários tamanhos com pelo menos
    # 64x64 de tamanho.
    
    biggestFace = detect_bounding_box(frame, face_classifier) # Descobrir oq é faces
    # Daqui pra frente usa faces ou frame?
    
    str = whatEmotion(biggestFace,model)
    drawString(str,frame)
    
    # --------------------A bagunça termina aqui
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()