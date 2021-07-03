# rotating
from PIL import Image, ImageFilter
img2 = Image.open(r"Image Path")
crooked = img2.rotate(180)
crooked.save("rotated.png", 'png')
