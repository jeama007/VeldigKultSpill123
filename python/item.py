import random as r

class Item:
    def __init__(self,name,description,attack,defense,health,ilvl):
        self.name = name
        self.description = description
        self.attack = attack
        self.defense = defense
        self.health = health
        self.ilvl = ilvl

    def __str__(self):
        print(f"{self.description}")

    def __repr__(self):
        return f"{self.name}"