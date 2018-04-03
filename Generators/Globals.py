ShipNames = ['Corvette','Cruiser','Battleship','Destroyer','Dreadgnought','Titan']


Ships = [('Corvette', 5), ('Cruiser', 10), ('Battleship', 20), ('Destroyer', 30), ('Dreadnought', 45), ('Titan', 100)]
ShipPath = '../Images/Ships/'

ShipPhotos = [ShipPath + 'Corvette.jpg',ShipPath + 'Cruiser.jpg',ShipPath + 'Battleship.jpg',
              ShipPath + 'Destroyer.jpg',ShipPath + 'Dreadgnought.jpg',ShipPath + 'Titan.jpg']

xEffects = [("Draw ", (2, 3, 4), " cards.", (20, 30, 40)),
            ("This turn you can buy up to ", (2, 3, 4), " ships.", (15, 30, 45)),
            ("Gain ", (50, 100, 150), " Credits.", (25, 50, 75)),
            ("If you won a war this turn gain ", (50, 100, 150), " Credits.", (15, 30, 45)),
            ("On a skirmish after revealing you can play this Card.Add ", (2, 3, 4), " ships to the skirmish.",
             (20, 30, 40)),
            ("This turn you can buy ", (2, 3, 4), " Science Cards.", (20, 30, 40)),
            ("After revealing you can play this card.Double the strength of all your ", ShipNames, 's', (75, 75, 75, 75, 75, 75)),
            ("After a player you skirmish with places ships face down you can activate this card.Reveal ", (2, 3, 4, 5),
             " ships randomly.", (20, 30, 40, 50))]
xEffectsNames = ["New Edicts", "Extra Shipyards", "Emergency Reserves", "Spoils of war", "Emergency FTL",
                 "Lots of Science",
                 "Extra firepower", "Big Sensors"]

EffectPath = '../Images/Effects/'
xEffectsPhotos = [EffectPath + 'NewEdicts.png',EffectPath + 'ExtraShipyards.jpg',EffectPath + 'EmergencyReserves.jpg',
                  EffectPath + 'SpoilsofWar.jpg',EffectPath + 'EmergencyFTL.jpg', EffectPath + 'LotsOfScience.jpg',
                  EffectPath + 'ExtraFirepower.jpg',EffectPath + 'BigSensors.jpg']



Effects = [("Select a player.Select a random card from his hand.Discard it.", 30),
           ("Select a player.Select a random ship from his fleet.Discard it", 45),
           ("Next time you collect resources take double those", 30),
           ("The next ship you buy this turn costs half", 20),
           ("Shuffle all science cards into the science deck and draw 5 new cards.", 10),
           ("Discard a card.Select a ship from the junkyard.You can buy it for half price.", 25),
           ("Shuffle all open ships into the shipyard and draw 5 new ships", 15),
           ("After a lost skirmish you can play this card.You lose no ships", 20),
           ("After revealing you can play this card.Double the strength of all your ships", 200),
           ("After a won skirmish you can play this card.Discard an extra ship", 45),
           ("Select a player.Take a ship from his fleet randomly", 100),
           ("Select a card from your discard pile.Add it to your hand", 55),
           ("When a player goes to war with you,you can play this card.Cancel the war", 15),
           ("Buy a ship from the junkyard", 35)]

EffectsNames = ["Sabotage", "Ship Termination", "Mining Overload", "Ship Recycling", "Research Grants", "Spaceship Finding",
                "Redesigns", "Retreat", "Firepower Overload", "Concentrated Firepower", "Seize the ships", "Recycling",
                "Peace", "Junk Ship"]

EffectPhotos = [EffectPath + 'Sabotage.jpg',EffectPath + 'ShipTermination.jpg', EffectPath + 'MiningOverload.jpg',
                EffectPath + 'ShipRecycling.jpg',EffectPath +'ResearchGrants.jpg',EffectPath + 'SpaceshipFinding.jpg',
                EffectPath + 'Redesigns.jpg',EffectPath + 'Retreat.jpg', EffectPath + 'FirepowerOverload.jpg',
                EffectPath + 'ConcentratedFirepower.jpg', EffectPath + 'SeizeTheShips.jpg',EffectPath + 'Recycling.jpg',
                EffectPath + 'Peace.jpg',EffectPath+ 'JunkShip.jpg']


SpaceNaziPath = '../Images/SpaceNazis/'
SpaceNaziBg = SpaceNaziPath + 'naziEarth.jpg'

SpaceUSSR = '../Images/SpaceUSSR/'
SpaceUSSRBg = SpaceUSSR + 'SpaceCommiesBg.jpg'

SpaceUSA = '../Images/SpaceMurica/'
SpaceUSABg = SpaceUSA + 'AmericaBg.jpg'

SpaceJapan = '../Images/SpaceJapan/'
SpaceJapanBg = SpaceJapan + 'JapanBg.jpg'

HeroShips = [('The Fuhrer\'s Titan',150,'If you win a skirmish with this card You win the war.', 200,SpaceNaziPath + 'HitlerTitan.jpg',SpaceNaziBg),
             ('Himler Dreadgnought',60,'This card\'s strength is equal to 100 if te controller is the attacker.',70,SpaceNaziPath +
              'HimlerDreadgnought.jpg',SpaceNaziBg),
             ('SS officer',20,'',35,SpaceNaziPath + 'SSofficer.jpg',SpaceNaziBg),
             ('Stalin Cruiser',50,'Once per turn you can show this card from your fleet to gain 10 Credits.',50,SpaceUSSR + 'StalinCruiser.jpg',SpaceUSSRBg),
             ('Lenin Battleship',30,'When you win a war with this card you can add Stalin Cruiser to your Hand(from anywhere)',20,SpaceUSSR + 'LeninBattleship.jpg',SpaceUSSRBg),
             ('Comrade',2,'',10,SpaceUSSR + 'Comrade.jpg',SpaceUSSRBg),
             ('Trump Titan',100,'When you buy this card add 2 mining station cards from your deck to the field',100,SpaceUSA + 'TrumpTitan.jpg',SpaceUSABg),
             ('Obama Battleship',30,'When you buy this card you can send a ship from your fleet to the scrapyard to gain 50 Credits',30,SpaceUSA + 'ObamaBattleship.jpg',SpaceUSABg),
             ('Muricans',10,'',20,SpaceUSA + 'murican.jpg',SpaceUSABg),
             ('Miyamoto Masashi',30,'After revealing you can add this card to the mobilized fleet from your fleet',30,SpaceJapan + 'MiyamotoMasashi.jpg',SpaceJapanBg),
             ('Dragon',20,'This card\'s strength is 60 if its controller is the defender',20,SpaceJapan + 'Dragon.png',SpaceJapanBg),
             ('Samurai',20,'',35,SpaceJapan + 'Samurai.jpg',SpaceJapanBg)]









ShipBackground = '../Images/Neutrals/ShipBackground.jpg'
NameBorder = '../Images/Neutrals/TextOutline.png'
PhotoOutline = '../Images/Neutrals/PhotoOutline.png'
EffOutline = '../Images/Neutrals/EffStrOutline.png'
CardOutline = '../Images/Neutrals/BackgroundBorder.png'

SpaceFont = '../Fonts/Nebulous-Regular.ttf'
DeathStarFont = '../Fonts/DeathStar.otf'


SaveShipPath = '../GeneratedCards/Ships/'
SaveSciencePath = '../GeneratedCards/Science/'
