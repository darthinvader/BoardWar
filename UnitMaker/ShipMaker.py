ShipNames = ['Frigate','Corvette','Cruiser','Galleon','Battleship','Battle Cruiser',
             'Assault Cruiser','Destroyer','Dreadnought','Man-o-war','Titan','WorldShip','BattleStar','Space Stations']
Types = {'Hull':'H','Armor':'A','Shield':'S'}
Weapons = ['Lasers','Neutron Torpedos','Mass Driver','Guided Missiles','Nuclear Missiles','Giga Cannon',
           'Perdition Beam','Black Hole Ballista']
StrengthMean = {'Frigate':10, 'Corvette':12, 'Cruiser':25,'Galleon':30,'BattleShip':40,'Battle Cruiser':50,'Swarm Carrier':80,
                'Assault Cruiser:':100 , 'Destroyer':120 , 'Dreagnough':150,'Man-o-war':200,'Titan':500,'WorldShip':1500,'BattleStar':5000,
                'Space Station':50}
WeaponMean = {'Lasers':('A',0.2),'Neutran Torpedos':('A',0.1,'S',0.3),'Mass Driver':('A',0.2,'2',0.4),'Guided Missiles':('A',0.2,'0,1 ',0.4),
              'Nuclear Missiles':('A',0.3,'A',0.5),'Giga Cannon':('A',0.3,'3,4',0.5),'Perdition Beam':('A',0.6),'Black Hole Ballista':('A',0.8)}


class Ship():

    def __init__(self,Strength,Mul,Range,Speed,BC,MC,Type,Effect):
        self.Strength = Strength
        self.Mul = Mul
        self.Range = Range
        self.Speed = Speed
        self.BC = BC
        self.Type = Type
        self.Effect = Effect
    def setName(self,Name):
        self.Name = Name






def GenerateShip():
    