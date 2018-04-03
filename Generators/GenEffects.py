from Generators.Globals import *
from ImageGen import Maker
from PIL import Image
class Effect():

    def __init__(self, Name, Effect, Cost, ImagePath,id):
        self.Name = Name
        self.Effect = Effect
        self.Cost = Cost
        self.ImagePath = ImagePath
        self.ID = id
    def setEffect(self, Effect):
        self.Effect = Effect

    def setCost(self, Cost):
        self.Cost = Cost

    def printEffect(self):
        print(self.Name, ",Science:", self.Effect, ",Cost:", self.Cost)

    def MakeEffectCard(self):
        ShipCard = Image.new('RGBA', Maker.CardSize, 'White')

        Maker.AddBg(ShipCard, ShipBackground)
        Maker.AddPhoto(ShipCard, self.ImagePath)
        Maker.AddCardBorder(ShipCard, CardOutline)
        Maker.AddNameBorder(ShipCard, NameBorder)
        Maker.AddCenterPhotoBorder(ShipCard, PhotoOutline)
        Maker.AddTextBorder(ShipCard, EffOutline)

        ShipCard = Maker.addName(ShipCard, self.Name)
        ShipCard = Maker.addCost(ShipCard, self.Cost)
        ShipCard = Maker.addEff(ShipCard, self.Effect)
        ShipCard.save(SaveSciencePath + self.Name + str(self.Cost) + self.Effect[0] + str(self.ID) +'.png','PNG')
        #ShipCard.show()


def GenerateXEffects():
    Xeffects = list()
    counter = -1
    for i in xEffects:
        counter = counter + 1
        for j in range(len(i[-1])):
            flag = True
            Stringer = ""
            for k in i:
                if isinstance(k,str):
                    Stringer = Stringer + k
                elif flag:
                    Stringer = Stringer + str(k[j])
                    flag = False
                else:
                    Xeffects.append(Effect(xEffectsNames[counter],Stringer,k[j],xEffectsPhotos[counter],j))
    return Xeffects

def GenerateNormal():
    Neffects = list()
    counter = 0
    for i in Effects:
        Neffects.append(Effect(EffectsNames[counter],i[0],i[1],EffectPhotos[counter],counter))
        counter += 1;
    return Neffects

def GenEffects():
    Xeffects = GenerateXEffects()
    Neffects = GenerateNormal()
    effects = Xeffects + Neffects
    return effects

def printEffects():
    effects = GenEffects()
    for i in effects:
        i.printEffect()


Effects = GenEffects()
for i in Effects[:]:
    i.MakeEffectCard()
