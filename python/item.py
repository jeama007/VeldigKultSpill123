import random as r
import python.spiller as spiller

class Item:
    def __init__(self, name, description, ilvl):
        self.name = name
        self.description = description
        self.ilvl = ilvl

    def __str__(self):
        return f"{self.description}"

    def __repr__(self):
        return f"{self.name}"

class Weapon(Item):
    def __init__(self, name, description, attack, ilvl):
        super().__init__(name, description, ilvl)
        self.attack = attack

    def __str__(self):
        return f"{self.description}"

class Armor(Item):
    def __init__(self, name, description, defense, ilvl):
        super().__init__(name, description, ilvl)
        self.defense = defense

class Mat(Item):
    def __init__(self, name,hpadd, description, ilvl):
        super().__init__(name, description, ilvl)
        self.hpadd = hpadd

    def __str__(self):
        return f"{self.description}"
    
    def helbredelse(self):
        spiller.hp += self.hpadd
        if spiller.hp > spiller.maxhp:
            spiller.hp = spiller.maxhp
    

def generateWeapon(name="", description="", attack=0, ilvl=0):
    name = name or f"{r.choice(weaponNamesPrefix)} {r.choice(weaponNamesSuffix)}"
    description = description or f"Våpenet du holder er {name}."
    attack = attack or 5 * ilvl
    return Weapon(name, description, attack, ilvl)

def generateArmor(name="", description="", defense=0, ilvl=0):
    name = name or f"{r.choice(armorNamesPrefix)} {r.choice(armorNamesSuffix)}"
    description = description or f"{name}."
    defense = defense or 3 * ilvl
    return Armor(name, description, defense, ilvl)

weaponNamesPrefix = ["Sword", "Axe", "Mace", "Spear", "Bow"]
weaponNamesSuffix = ["of the Monkey", "of the Tiger", "of the Bear", "of the Wolf", "of the Eagle"]

armorNamesPrefix = ["Hjelm", "Brystplate", "Bukse", "Sko"]
armorNamesSuffix = ["av skogen", "av himmelen", "av flamme", "av fjellet"]