import numpy as np
from PIL import Image, ImageDraw, ImageFont
from Generators.Globals import *

NeutralPos = (0, 0)
CardSize = (1200, 1700)
PhotoSize = (1000, 800)
NamePos = (100, 70)
PhotoPos = (100, 270)
EffStrPos = (100, 1120)
TextPos = (120,105)

def ShipCard(ShipName,ImagePath):
    # size = (1700, 1200)
    FontLoad = ImageFont.truetype(SpaceFont, 100)

    ShipCard = Image.new('RGBA', CardSize, 'White')
    ShipPhoto = (Image.open(ImagePath)).resize(PhotoSize, Image.ANTIALIAS)
    ShipCardBg = (Image.open(ShipBackground)).resize(CardSize, Image.ANTIALIAS)
    NameCardBorder = (Image.open(NameBorder))
    CardBorder = (Image.open(CardOutline))
    PhotoBorder = (Image.open(PhotoOutline))
    EffBorder = (Image.open(EffOutline))

    ShipCard.paste(ShipCardBg, NeutralPos, None)
    ShipCard.paste(ShipPhoto, PhotoPos, None)
    ShipCard.paste(CardBorder, NeutralPos, CardBorder)
    ShipCard.paste(NameCardBorder, NamePos, NameCardBorder)
    ShipCard.paste(PhotoBorder, PhotoPos, PhotoBorder)
    ShipCard.paste(EffBorder, EffStrPos, EffBorder)

    txtImage = Image.new('RGBA', ShipCard.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(txtImage)
    d.text(TextPos, ShipName, font=FontLoad, fill=(255, 255, 255, 255))
    out = Image.alpha_composite(ShipCard, txtImage)
    out.show()


ShipCard("Corvette","../Images/Ships/Corvette.jpg")
