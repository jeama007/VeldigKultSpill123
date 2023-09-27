class spiller:
    def __init__(self, navn, weapon, armor):
        self.navn = navn
        self.hp = 100
        self.weapon = weapon
        self.armor = armor
    
    def damage(self, dmg):#funksjon for spillerskade
        self.hp = self.hp - dmg
    
    def setWeapon(self, pickup):
        self.weapon = pickup
    
    def setArmor(self, pickup):
        self.armor = pickup