### Objetivo
Este projeto busca apontar 5 emoções do rosto humano a partir de um vídeo ou câmera com a ajuda do dataset AffectNet.

*Projeto em desenvolvimento*: a precisão do modelo ainda está por volta de 50% e o código responsável pela aplicação do modelo em vídeos não está completo.

### Treinos no Kaggle
Para utilizar os códigos mais recentes (TreinoKaggle.ipynb e my2emotionsmodel.ipynb), que estão em src/treinos, basta utilizar o espaço para programação do Kaggle e importar o Affect Net pela plataforma.
- TreinoKaggle.ipynb é o treinamento feito do zero e sua precisão não passa de 50%.
- my2emotionsmodel.ipynb é um treinamento que utiliza Resnet50 e ainda está em desenvolvimento, pois seu resultado é insatisfatório.

### Código de alteração de vídeos
Os arquivos main.py e utils.py são responsáveis por detectar a posição do rosto a cada quadro do vídeo e entregar esta imagem ao modelo, mas ainda não estão finalizados.

### Treino no Google Colab
Para utilizar o código do colab (src/Treinos/TreinoColab.ipynb), que está desatualizado, primeiramente crie uma pasta "Data" no ColabNotebooks do seu google drive, e deposite a chave API kaggle.json. O segundo vídeo da bibliografia explica bem.
Além disto, o caminho "Colab Notebooks" precisa estar como "ColabNotebooks".

### Bibliografia:
- https://numpy.org/doc/stable/reference/generated/numpy.argmax.html
- https://www.youtube.com/watch?v=yEXkEUqK52Q
- https://www.kaggle.com/datasets/thienkhonghoc/affectnet/code
- https://stackoverflow.com/questions/33650974/opencv-python-read-specific-frame-using-videocapture
- Aula 06, 08 e 12 - Visão computacional FEI.
- https://www.datacamp.com/tutorial/face-detection-python-opencv
- https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
- https://www.tensorflow.org/tutorials/keras/classification?hl=pt-br
- https://stackoverflow.com/questions/61377545/is-there-a-way-to-draw-the-replacement-character-symbol-on-an-image-using-cv2
- https://github.com/python-pillow/Pillow/issues/2695
- https://github.com/PyImageSearch/imutils/blob/master/imutils/paths.py
