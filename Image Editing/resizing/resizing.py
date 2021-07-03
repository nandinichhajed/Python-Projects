# resizing
from PIL import Image, ImageFilter
img3 = Image.open(r"Image Path")
print(img3.size)
resize = img3.resize((160, 149))
resize.save("resized.png", 'png')
