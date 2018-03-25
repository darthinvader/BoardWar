from PIL import Image

#def imageMaker():
im = Image.open("Toilet.png")
im.rotate(45).show()