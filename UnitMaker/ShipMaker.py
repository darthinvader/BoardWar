ShipNames = ['Frigate','Corvette','Cruiser','Galleon','Battleship','Battle Cruiser',
             'Assault Cruiser','Destroyer','Dreadnought','Man-o-war','Titan','WorldShip','BattleStar','Space Stations']
StrengthMean = {'Frigate':(2,10), 'Corvette':(2,12), 'Cruiser':(5,25),'Galleon':(8,30),'BattleShip':(10,40),'Battle Cruiser':(15,50),
                'Swarm Carrier':(10,80),'Assault Cruiser:':(20,100), 'Destroyer':(40,120), 'Dreagnough':(60,150),
                'Man-o-war':(50,200),'Titan':(120,500),'WorldShip':(300,1500),'BattleStar':(1000,5000),'Space Station':(10,50)}

class Ship():

    def __init__(self,Name,Attack,Health,Range,Speed,BC):
        self.Name = Name
        self.Attack = Attack
        self.Health = Health
        self.Range = Range
        self.Speed = Speed
        self.BC = BC





def GenerateShip():
