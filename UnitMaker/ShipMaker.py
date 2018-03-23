from numpy.random import normal
from numpy import random
from math import ceil
import copy
ShipNames = ['Frigate','Corvette','Cruiser','Galleon','Battleship','Battle Cruiser',
             'Assault Cruiser','Destroyer','Dreadnought','Man-o-war','Titan','WorldShip','BattleStar',
             'Space Station','Station Cannon','Station Beam']
StrengthMean = {'Frigate':(2,10,1,1), 'Corvette':(2,12,1,1), 'Cruiser':(5,25,1,1),'Galleon':(8,30,1,2),'Battleship':(10,40,2,2),'Battle Cruiser':(15,50,2,2),
                'Swarm Carrier':(10,80,1,2),'Assault Cruiser':(20,100,2,2), 'Destroyer':(40,120,1,2), 'Dreadnought':(60,150,3,2),
                'Man-o-war':(50,200,2,3),'Titan':(120,500,3,2),'WorldShip':(300,1500,3,1),'BattleStar':(1000,5000,3,1),
                'Space Station':(10,50,3,0),'Station Cannon':(10,50,3,0),'Station Beam':(20,20,3,0)}
EffectNames = ['Rush','Black Hole Ballista','Perdition Beam','Swarm','Core Overload']
Effects = {'Rush':1.2,'Black Hole Ballista':1.8,'Perdition Beam':1.5,'Swarm':2,'Core Overload':1.5}



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



