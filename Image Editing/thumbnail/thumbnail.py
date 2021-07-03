from PIL import Image, ImageFilter
img = Image.open(r"Image Path")
img.thumbnail((400, 400))
img.save(('thumbnail.jpg'))
print(img.size)
