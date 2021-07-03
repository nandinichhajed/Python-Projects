from PIL import Image, ImageFilter

img = Image.open(r"Image Path")

print(img)
print(img.format)
print(img.size)
print(img.mode)
# print(dir(img))

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img = img.filter(ImageFilter.SHARPEN)


filtered_img.save("blur.png", 'png')
filtered_img.save("smooth.png", 'png')
filtered_img.save("sharpen.png", 'png')
