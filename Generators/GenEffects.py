from Generators.Globals import *

class Effect():
    def __init__(self, Name, Effect, Cost):
        self.Name = Name
        self.Effect = Effect
        self.Cost = Cost

    def setEffect(self, Effect):
        self.Effect = Effect

    def setCost(self, Cost):
        self.Cost = Cost

    def printEffect(self):
        print(self.Name, ",Effect:", self.Effect, ",Cost:", self.Cost)




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
                    Xeffects.append(Effect(xEffectsNames[counter],Stringer,k[j]))
    return Xeffects

def GenerateNormal():
    Neffects = list()
    counter = 0
    for i in Effects:
        Neffects.append(Effect(EffectsNames[counter],i[0],i[1]))
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


printEffects()