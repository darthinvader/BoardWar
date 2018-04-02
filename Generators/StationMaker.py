from ImageGen import Maker
from Generators.Globals import *

class Station():
    def __init__(self, Name, Strength, BC, ImagePath):
        self.Name = Name
        self.Strength = Strength
        self.BC = BC
        self.ImagePath = ImagePath
    def setEffect(self, Effect):
        self.Effect = Effect

    def setCost(self, Cost):
        self.Cost = Cost

    def printShip(self):
        print(self.Name, ",Strength:", self.Strength, ",BC:", self.BC)

    def MakeShipCard(self):
        ShipCard = Image.new('RGBA', Maker.CardSize, 'White')

        Maker.AddBg(ShipCard, ShipBackground)
        Maker.AddPhoto(ShipCard, self.ImagePath)
        Maker.AddCardBorder(ShipCard, CardOutline)
        Maker.AddNameBorder(ShipCard, NameBorder)
        Maker.AddCenterPhotoBorder(ShipCard, PhotoOutline)
        Maker.AddTextBorder(ShipCard, EffOutline)

        ShipCard = Maker.addName(ShipCard, self.Name)
        ShipCard = Maker.addCost(ShipCard, self.BC)
        ShipCard = Maker.addStr(ShipCard, self.Strength)
        ShipCard.save(SaveShipPath + self.Name + str(self.BC) + str(self.Strength) + '.png','PNG')
        #ShipCard.show()


