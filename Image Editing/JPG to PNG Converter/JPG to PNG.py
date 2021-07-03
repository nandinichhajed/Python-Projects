from PIL import Image

image = Image.open(r'Image Path')
image.save("changed.png", 'png')
