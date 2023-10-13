import random as r

class Item:
    def __init__(self,name,description,attack,ilvl): # lager en konstruktør som tar inn navn, beskrivelse, ilvl. Ilvl er item level, som er en verdi som bestemmer hvor bra et item er. Tenkte at denne kunne skalere med hvilket rom du finner item i, og bruke den til å bestemme hvor høye de andre statsene er.
        self.name = name
        self.description = description
        self.ilvl = ilvl

    def __str__(self):
        return f"{self.description}" + f"Dette itemet har {self.attack} attack og {self.defense} defense."
    
    def __repr__(self):
        return f"{self.name}"
    

class Weapon(Item):
    def __init__(self,name,description,attack,ilvl):
        super().__init__(name,description,attack,ilvl)
        self.attack = attack

    def __str__(self):
        return f"{self.description}"

class Armor(Item):
    def __init__(self,name,description,defense,ilvl):
        super().__init__(name,description,defense,ilvl)
        self.defense = defense

weaponNamesPrefix = ["Sword","Axe","Mace","Spear","Bow",]
weaponNamesSuffix = ["of the Monkey","of the Tiger","of the Bear","of the Wolf","of the Eagle"]

armorNamesPrefix = ["Hjelm","Brystplate","Bukse","Sko"]
armorNamesSuffix = ["av skogen","av himmelen","av flamme","av fjellet"]

def generateWeapon(name="",description="",attack=0,ilvl=0):
    if name == "":
        name = f"{weaponNamesPrefix} {weaponNamesSuffix}"
    if description == "":
        description = "Våpenet du holder er" + name + "."
    if attack == 0:
        attack = 5*ilvl
    if ilvl == 0:
        ilvl = ilvl
    return Weapon(name,description,attack,ilvl)

def generateArmor(name="",description="",defense=0,ilvl=0):
    if name == "":
        name = "{} {}".format(r.choice(armorNamesPrefix),r.choice(armorNamesSuffix))
    if description == "":
        description = "" + name + "."
    if defense == 0:
        defense = 3*ilvl
    if ilvl == 0:
        ilvl = ilvl
    return Armor(name,description,defense,ilvl)

