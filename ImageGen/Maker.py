import numpy as np
from PIL import Image

CardSize = (1700, 1200)
PhotoSize = (1000, 800)
PhotoPos = (100,100)

def ShipCard(ImagePath):
    # size = (1700, 1200)
    ShipImage = Image.new('RGBA', CardSize, 'White')
    Photo = (Image.open(ImagePath)).resize(PhotoSize, Image.ANTIALIAS)
    ShipImage.paste(Photo, (100, 0), Photo)
    ShipImage.show()

    del Photo


# Convert Image to array


ShipCard("foo.png")

# shape = (1700,1200,4)
# arr = np.ndarray(shape,)
#
# arr = np.array(arr)
# for i in arr:
#     for j in i:
#             j[0] = np.random.normal(0, 50)
#             if j[0]>255:
#                 j[0] = 255
#             if j[0]<0:
#                 j[0] = 0
#             j[1] = 0#(np.random.normal(122, 10)%255)
#             j[2] = 0#(np.random.normal(122, 10)%255)
#             j[3] = 100
#
#
# print(arr)
#
#
# im = Image.fromarray(np.uint8(arr))
#
# im.show()
