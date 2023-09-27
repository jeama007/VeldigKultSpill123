import random as r

class Item:
    def __init__(self,name,description,attack,ilvl): # lager en konstruktør som tar inn navn, beskrivelse, ilvl. Ilvl er item level, som er en verdi som bestemmer hvor bra et item er. Tenkte at denne kunne skalere med hvilket rom du finner item i, og bruke den til å bestemme hvor høye de andre statsene er.
        self.name = name
        self.description = description
        self.ilvl = ilvl

    def __str__(self):
        print(f"{self.description}")

    def __repr__(self):
        return f"{self.name}"
    

class Weapon(Item):
    def __init__(self,name,description,attack,ilvl):
        super().__init__(name,description,attack,ilvl)
        self.attack = attack

class Armor(Item):
    def __init__(self,name,description,defense,ilvl):
        super().__init__(name,description,defense,ilvl)
        self.defense = defense

weaponNamesPrefix = ["Sword","Axe","Mace","Spear","Bow",]
weaponNamesSuffix = ["of the "]

armorNamesPrefix = ["Helmet","Chestplate","Leggings","Boots"]
armorNamesSuffix = ["of the ancient","of the old","of the new","of the forgotten"]

def generateWeapon():
    name = "{} {}".format(weaponNamesPrefix[r.randint(1,5)],r.choice(weaponNamesSuffix))
    description = "This is a " + name + "."
    attack = r.randint(1,10)
    ilvl = r.randint(1,10)
    return Weapon(name,description,attack,ilvl)

currentWeapon = generateWeapon()
print(currentWeapon.description)