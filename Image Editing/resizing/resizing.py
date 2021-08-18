# resizing
from PIL import Image, ImageFilter
img3 = Image.open(r"File path")
print(img3.size)
resize = img3.resize((550, 500))
resize.save("new.png", 'png')
