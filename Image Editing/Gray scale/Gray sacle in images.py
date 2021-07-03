from PIL import Image, ImageFilter
img2 = Image.open(r"Image Path")
filtered_img = img2.convert('L')  # L -> Gray scale
filtered_img.save("gray.png", 'png')
filtered_img.show()
