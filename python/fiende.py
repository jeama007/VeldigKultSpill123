import random as r
import item as item
class Fiende:
    def __init__(self, navn, hp, damage, forsvar):
        self.navn = navn
        self.hp = hp
        self.damage = damage
        self.forsvar = forsvar

    def fiende_damage(self, dmg): # Funksjon for at fienden skal ta skade.
        self.hp = self.hp - dmg

# Verdier er ikke endelige, bare placeholder

listemednavn = ["Nisse", "Kjempe", "Ridder", "Ulv", "Boksman"]

def nyFiende(nivå):
    fiende = Fiende(r.choice(listemednavn), 10*nivå, nivå, nivå/2)
    return fiende

def fiendeDør():
    fiendevåpen = item.generateWeapon()
    print("Fienden døde!")
    print("Fienden slapp et våpen: " + fiendevåpen.navn)
    

    pass
"""
nisse = Fiende("Nisse", 50, 5, 1) # Svak fiende

ulv = Fiende("Ulv", 40, 10, 1) # Svak fiende med litt hoy skade

ridder = Fiende("Ridder", 70, 10, 10) # Noe hoyere skade med mye forsvar

kjempe = Fiende("Kjempe", 150, 15, 1) # Mye hp og medium-hoy skade. Ikke mye forsvar. Mini-boss
"""
boks_man = Fiende("Boks Man", 100, 5, 20) # Mye forsvar, lav skade.

