# croping
from PIL import Image, ImageFilter
img4 = Image.open(r"Image Path")
print(img4.size)
box = (100, 100, 400, 400)
region = img4.crop(box)
region.save("cropped.png", 'png')
