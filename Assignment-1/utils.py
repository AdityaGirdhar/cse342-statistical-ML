from PIL import Image
from numpy import asarray

def flattenImage(path):
    image = Image.open(path)
    data = asarray(image)
    imgArray = []
    for i in data:
        for j in i:
            imgArray.append(j)
    return imgArray

