from numpy.random import normal
from numpy import random
from math import ceil
from Generators.Globals import *
import copy



class Ship():
    def __init__(self,Name,Attack,Health,Range,Speed,Cost,Effect):
        self.Name = Name
        self.Attack = Attack
        self.Health = Health
        self.Range = Range
        self.Speed = Speed
        self.Cost = Cost
        self.Effect = Effect
    def setEffect(self,Effect):
        self.Effect = Effect

    def setCost(self,Cost):
        self.Cost =Cost

    def printShip(self):
        print(self.Name , ",Attack:", self.Attack,",Health:", self.Health, ",Range:", self.Range,
              ",Speed:",self.Speed,",Cost:",self.Cost,",Effect:",self.Effect)


def GenerateShip(ShipName):
    means = StrengthMean[ShipName]
    attack = -1
    while attack<=0:
        attack = normal(means[0],means[1]/8)
    if attack <=40:
        attack = ceil(attack)
    elif attack <=400:
        attack = ceil(attack/10)*10
    else:
        attack = ceil(attack/100)*100
    health = -1
    while health<=0:
        health = normal(means[1],means[1]/6)

    if health <=40:
        health = ceil(health)
    elif health<=400:
        health = ceil(health/10)*10
    else:
        health = ceil(health/100)*100
    if means[2] == 1:
        range = 1
    else:
        range = random.randint(1,means[2])
    if means[3] == 0:
        speed = 0
    elif means[3] == 1:
        speed = 1
    else:
        speed = random.randint(1,means[3])
    effect = ''

    cost = ceil(attack*health*(1+speed/5)*(1+range/3)/20)

    ship = Ship(ShipName,attack,health,range,speed,cost,effect)
    return ship

def GenerateHero(ship):
    ship = copy.deepcopy(ship)
    EffectName = EffectNames[(random.randint(1,len(Effects)))]
    effect = Effects[EffectName]

    ship.setEffect(EffectName)
    ship.setCost(ship.Cost*effect)
    return ship

def GenerateFleet():
    ships = list()
    for i in ShipNames:
        ships.append(GenerateShip(i))
        ships[-1].printShip()
    print()
    heroes = list()
    for i in ships:
        heroes.append(GenerateHero(i))
        heroes[-1].printShip()



GenerateFleet()