from Generators.Globals import *
from PIL import Image
from ImageGen import Maker


class Hero():
    def __init__(self, Name,  BC,Effect,Strength, ImagePath,Bg):
        self.Name = Name
        self.Strength = Strength
        self.BC = BC
        self.Effect = Effect
        self.ImagePath = ImagePath
        self.Bg = Bg
    def setEffect(self, Effect):
        self.Effect = Effect

    def setCost(self, Cost):
        self.Cost = Cost

    def printShip(self):
        print(self.Name, ",Strength:", self.Strength, ",BC:", self.BC)

    def MakeShipCard(self):
        ShipCard = Image.new('RGBA', Maker.CardSize, 'White')

        Maker.AddBg(ShipCard, self.Bg)
        Maker.AddPhoto(ShipCard, self.ImagePath)
        Maker.AddCardBorder(ShipCard, CardOutline)
        Maker.AddNameBorder(ShipCard, NameBorder)
        Maker.AddCenterPhotoBorder(ShipCard, PhotoOutline)
        Maker.AddTextBorder(ShipCard, EffOutline)

        ShipCard = Maker.addName(ShipCard, self.Name)
        ShipCard = Maker.addCost(ShipCard, self.BC)
        ShipCard = Maker.addStr(ShipCard, self.Strength)
        if self.Effect != '':
            ShipCard = Maker.addEff(ShipCard, self.Effect)
        ShipCard.save(SaveShipPath + self.Name + str(self.BC) + str(self.Strength) + '.png','PNG')

herolist = list()

for i in HeroShips:
    herolist.append(Hero(i[0],i[1],i[2],i[3],i[4],i[5]))

for i in herolist:
    i.MakeShipCard()