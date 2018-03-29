from numpy.random import normal
from numpy import random
from numpy import exp
from math import ceil,floor,sqrt
from Generators.Globals import *
from numpy import log2
import copy


class Ship():
    def __init__(self, Name, Strength, BC, Effect):
        self.Name = Name
        self.Strength = Strength
        self.BC = BC
        self.Effect = Effect

    def setEffect(self, Effect):
        self.Effect = Effect

    def setCost(self, Cost):
        self.Cost = Cost

    def printShip(self):
        print(self.Name, ",Strength:", self.Strength, ",BC:", self.BC, ",Effect:", self.Effect)


def GenerateShip(ShipName):
    mean = StrengthMean[ShipName]
    strength = ceil(normal(mean, mean / 5))
    if strength <= 1:
        strength = 1
    BC = ceil(normal(strength, mean / 10))
    if BC <= 1:
        BC = 1
    ship = Ship(ShipName, strength, BC, '')
    return ship


# def GenerateHero(ship):


def GenerateFleet():
    ships = list()
    for i in ShipNames:
        ships.append(GenerateShip(i))
        ships[-1].printShip()
    return ships
    print()

    # heroes = list()
    # for i in ships:
    #     heroes.append(GenerateHero(i))
    #     heroes[-1].printShip()


GenerateFleet()
