import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFont, ImageDraw

#Função: Entra o frame do vídeo e o classificador e sai algo que eu não tenho a mínima ideia do que é.
def detect_bouding_box(frame, face_classifier):
    faces = face_classifier.detectMultiScale(
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), # Frame do vídeo sem cor.
                     1.1,               #Imagens serão reduzidas em 10% (facilitar detecção).
                     5,                 #Retângulos vizinhos necessários para validar detecção.
                     minSize=(80, 80)   # Mínimo tamanho para um objeto ser detectado.
                     )
    # Objetivo: retornar imagem cortada do maior rosto com margem de 20%
    x1 = []
    y1 = []
    w1 = []
    h1 = []
    
    for (x, y, w, h) in faces:
        x1.append(x)
        y1.append(y)
        w1.append(w)
        h1.append(h)
    
    biggest = []
    for (x,y,w,h) in (x1,y1,w1,h1):
        if len(biggest) == 0:
            biggest.append(x)
            biggest.append(y)
            biggest.append(w)
            biggest.append(h)
        
        else:
            val = (w)*(h)
            if val > (biggest[2]*biggest[3]):
                biggest.clear()
                biggest.append(x)
                biggest.append(y)
                biggest.append(w)
                biggest.append(h)
                
            else:
                continue
                     
    # imgCrop =>    x:               x+w,               y:              y+h
    return frame[ biggest[0]:biggest[0]+biggest[2], biggest[1]:biggest[1]+biggest[3] ]


# Fução: Entra imagem recortada e saí string, utiliza o modelo para isto.
def whatEmotion(frame, model):
    frame = cv2.resize(frame, (80, 80))
    data = np.array(frame, dtype="float") / 255.0
    print("Formato da imagem",data.shape)
    
    print("Generating test predictions...")
    
    # predict_x retorna um array de tamanho 5, com um valores 0 < x < 1
    predict_x= model.predict(data)
    # Exemplo [[3.2807174e-07 1.0875438e-09 4.7872772e-10 1.3293584e-10 4.8750932e-09]]
    
    # argmax retorna o index do maior número encontrado.
    match np.argmax(predict_x):
        case 0:
            return "Angry"
        case 1:
            return "Happy"
        case 2:
            return "Sad"
        case 3:
            return "Surprised"
        case 4:
            return "Neutral"
        case _:
            return "Error"
    
    
#Função: Entra uma string e desenha ela com CV2.
def drawString(string,frame):
    # Open image with OpenCV
    #im_o = cv2.imread('start.png')

    # Make into PIL Image
    im_p = Image.fromarray(frame)

    # Get a drawing context
    draw = ImageDraw.Draw(im_p)
    font = ImageFont.load_default()
    draw.text((40, 20),string,(255,255,255),font=font)

    # Convert back to OpenCV image and save
    cv2.imshow("Tá funcionando?",np.array(im_p))
    