from numpy.random import normal
from math import ceil
from Generators.Globals import *
from PIL import Image
from ImageGen import Maker

class Ship():
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
        ShipCard.show()

def GenerateShip(ShipNum):
    mean = Ships[ShipNum][1]
    ShipName = Ships[ShipNum][0]
    strength = ceil(normal(mean, mean / 5))
    if strength <= 1:
        strength = 1
    BC = ceil(normal(strength, mean / 10))
    if BC <= 1:
        BC = 1
    ship = Ship(ShipName, strength, BC, ShipPhotos[ShipNum])
    return ship


# def GenerateHero(ship):


def GenerateFleet():
    ships = list()
    for i in range(0, len(Ships)):
        ships.append(GenerateShip(i))
        ships[-1].printShip()
    return ships

    # heroes = list()
    # for i in ships:
    #     heroes.append(GenerateHero(i))
    #     heroes[-1].printShip()


ships = GenerateFleet()
