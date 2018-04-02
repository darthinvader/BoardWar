from PIL import Image, ImageDraw, ImageFont
from Generators.Globals import *
import math
import textwrap

NeutralPos = (0, 0)
CardSize = (1200, 1700)
PhotoSize = (1000, 800)
NamePos = (100, 70)
PhotoPos = (100, 270)
EffStrPos = (100, 1120)

NameTxtMid = (150,145)

TextPos = (120, 105)
NameMaxHeight = 100
NameMaxWidth = 700
CostMaxSize = (150,100)
CostPosMid = (1000,145)

StrMaxSize = (800,100)
StrPosMid = (600,1530)

EffMaxSize = (800,300)
EffPosMid = (600,1150)



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



def FindSingleLineFontSize(text,font,maxTxtSize,maxFontSize):
    FontLoad = ImageFont.truetype(font, 100)
    txtImage = Image.new('RGBA', CardSize, (255, 255, 255, 0))
    d = ImageDraw.Draw(txtImage)
    txtsize = d.textsize(text, FontLoad)
    txtWidth = txtsize[0] / 100
    txtHeight = txtsize[1] / 100
    fontWidth = math.floor(maxTxtSize[0]/txtWidth)
    fontHeight = math.floor(maxTxtSize[1]/txtHeight)

    if fontWidth>fontHeight:
        fontSize = fontHeight
    else:
        fontSize = fontWidth
    if fontSize>maxFontSize:
        fontSize = maxFontSize

    FontLoad = ImageFont.truetype(font, fontSize)
    txtsize = d.textsize(text, FontLoad)

    return fontSize, txtsize



def FindNameFontSize(text):
    return FindSingleLineFontSize(text,SpaceFont,(NameMaxWidth,NameMaxHeight),90)

def getNamePos(txtSize):
    height = NameTxtMid[1] - txtSize[1]/2
    width = NameTxtMid[0]
    return (width,height)

def addName(CardImage,Name):
    fontSize,txtsize = FindNameFontSize(Name)
    pos = getNamePos(txtsize)


    txtImage = Image.new('RGBA', CardSize, (255, 255, 255, 0))
    d = ImageDraw.Draw(txtImage)
    FontLoad = ImageFont.truetype(SpaceFont, fontSize)
    d.text(pos,Name,font=FontLoad,fill=(255,255,255,255))
    out = Image.alpha_composite(CardImage,txtImage)
    return out

def FindCostFontSize(Cost):
    return FindSingleLineFontSize(Cost,DeathStarFont,CostMaxSize,90)

def getCostPos(txtSize):
    height = CostPosMid[1] - txtSize[1] / 2
    width = CostPosMid[0] - txtSize[0]/2
    return (width, height)


def addCost(CardImage,Cost):
    Cost = str(Cost)
    fontSize,txtSize = FindCostFontSize(Cost)
    pos = getCostPos(txtSize)
    txtImage = Image.new('RGBA', CardSize, (255, 255, 255, 0))
    d = ImageDraw.Draw(txtImage)
    FontLoad = ImageFont.truetype(DeathStarFont, fontSize)
    d.text(pos, Cost, font=FontLoad, fill=(255, 255, 255, 255))
    out = Image.alpha_composite(CardImage, txtImage)
    return out

def FindStrFontSize(Str):
    return FindSingleLineFontSize(Str, DeathStarFont, StrMaxSize, 130)

def getStrPos(txtSize):
    height = StrPosMid[1] - txtSize[1] / 2
    width = StrPosMid[0] - txtSize[0]/2
    return (width, height)

def addStr(CardImage,Str):
    Str = 'Str: ' + str(Str)
    fontSize,txtSize = FindStrFontSize(Str)
    pos = getStrPos(txtSize)
    txtImage = Image.new('RGBA', CardSize, (255, 255, 255, 0))
    d = ImageDraw.Draw(txtImage)
    FontLoad = ImageFont.truetype(DeathStarFont, fontSize)
    d.text(pos, Str, font=FontLoad, fill=(255, 255, 255, 255))
    out = Image.alpha_composite(CardImage, txtImage)
    return out

def FindEffFontSize(primer,Lines):
    return FindSingleLineFontSize(primer,DeathStarFont,(EffMaxSize[0],EffMaxSize[1]/Lines),1000)

def getLinePos(Line,LineNum,TotalLines,fontSize):
    print(fontSize)
    FontLoad = ImageFont.truetype(DeathStarFont, fontSize)
    txtImage = Image.new('RGBA', CardSize, (255, 255, 255, 0))
    d = ImageDraw.Draw(txtImage)
    txtsize = d.textsize(Line, FontLoad)
    txtWidth = txtsize[0]
    txtHeight = txtsize[1]
    LinePos = (EffPosMid[0] - txtWidth/2,EffPosMid[1] + (300/TotalLines)*LineNum)
    return LinePos

def addEff(CardImage,Eff):
    Eff = textwrap.fill(Eff,width=100)
    primer = Eff[0]
    fontSize,txtSize = FindEffFontSize(primer,len(Eff))
    i=0
    out = CardImage
    for line in Eff:
        pos = getLinePos(line,i,len(Eff),fontSize)
        txtImage = Image.new('RGBA', CardSize, (255, 255, 255, 0))
        d = ImageDraw.Draw(txtImage)
        FontLoad = ImageFont.truetype(DeathStarFont, fontSize)
        d.text(pos, line, font=FontLoad, fill=(255, 255, 255, 255))
        out = Image.alpha_composite(out, txtImage)
        i += 1
    return out

def ShipCard(ShipName,BC,Str,Eff,ImagePath):
    # size = (1700, 1200)
    FontLoad = ImageFont.truetype(SpaceFont, 100)

    ShipCard = Image.new('RGBA', CardSize, 'White')

    AddBg(ShipCard,ShipBackground)
    AddPhoto(ShipCard,ImagePath)
    AddCardBorder(ShipCard,CardOutline)
    AddNameBorder(ShipCard,NameBorder)
    AddCenterPhotoBorder(ShipCard,PhotoOutline)
    AddTextBorder(ShipCard,EffOutline)

    ShipCard = addName(ShipCard,ShipName)
    ShipCard = addCost(ShipCard,BC)
    ShipCard = addStr(ShipCard,Str)
    ShipCard = addEff(ShipCard,Eff)
    ShipCard.show()

    # print(d.textsize(ShipName,FontLoad))

ShipCard("I am the FUHRER",5,1,"I DEMAND MORE CHOCOLATE ","../Images/Ships/Corvette.jpg")
