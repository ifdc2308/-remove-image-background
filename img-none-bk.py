#pip install pillow
#pip install rembg

from rembg import remove
from PIL import Image

#input imagem original
img = Image.open('img.jpg')

#removendo fundo da img
img_whitout_back = remove(img)

#salvando imagem sem o fundo
img_whitout_back.save('image_sem_fundo.png')
