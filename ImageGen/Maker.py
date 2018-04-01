import numpy as np
from PIL import Image, ImageDraw, ImageFont
from Generators.Globals import *

NeutralPos = (0, 0)
CardSize = (1200, 1700)
PhotoSize = (1000, 800)
NamePos = (100, 70)
PhotoPos = (100, 270)
EffStrPos = (100, 1120)
TextPos = (120, 105)
NameMaxHeight = 100
NameMaxWidth = 700



def AddBg(CardImage,Bg):
    CardBg = (Image.open(Bg)).resize(CardSize, Image.ANTIALIAS)
    CardImage.paste(CardBg,NeutralPos,None)

def AddCardBorder(CardImage,CBorder):
    BorderImage = (Image.open(CBorder)).resize(CardSize, Image.ANTIALIAS)
    CardImage.paste(BorderImage,NeutralPos,BorderImage)

def AddPhoto(CardImage,Photo):
    CenterPhoto = (Image.open(Photo)).resize(PhotoSize, Image.ANTIALIAS)
    CardImage.paste(CenterPhoto,PhotoPos,None)

def AddNameBorder(CardImage,NameBorder):
    NameBorderImage = Image.open(NameBorder)
    CardImage.paste(NameBorderImage,NamePos,NameBorderImage)

def AddCenterPhotoBorder(CardImage,PhotoBorder):
    PhotoCenterBorder = Image.open(PhotoBorder)
    CardImage.paste(PhotoCenterBorder,PhotoPos,PhotoCenterBorder)

def AddTextBorder(CardImage,TextBorder):
    TextBorderImage = Image.open(TextBorder)
    CardImage.paste(TextBorderImage,EffStrPos,TextBorderImage)

def AddName(CardImage,text):
    FontLoad = FontLoad = ImageFont.truetype(SpaceFont, 100)
    txtImage = Image.new('RGBA', ShipCard.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(txtImage)
    txtsize = d.textsize(text,FontLoad)
    txtWidth = txtsize[0]/100
    txtHeight = txtsize[1]/100

    fontWidth = NameMaxWidth/txtWidth
    fontHeight = NameMaxHeight/txtHeight




def ShipCard(ShipName,ImagePath):
    # size = (1700, 1200)
    FontLoad = ImageFont.truetype(SpaceFont, 100)

    ShipCard = Image.new('RGBA', CardSize, 'White')

    AddBg(ShipCard,ShipBackground)
    AddPhoto(ShipCard,ImagePath)
    AddCardBorder(ShipCard,CardOutline)
    AddNameBorder(ShipCard,NameBorder)
    AddCenterPhotoBorder(ShipCard,PhotoOutline)
    AddTextBorder(ShipCard,EffOutline)

    txtImage = Image.new('RGBA', ShipCard.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(txtImage)
    d.text(TextPos, ShipName, font=FontLoad, fill=(255, 255, 255, 255))
    out = Image.alpha_composite(ShipCard, txtImage)
    out.show()
    print(d.textsize(ShipName,FontLoad))

ShipCard("Corvette","../Images/Ships/Corvette.jpg")
