class spiller:
    def __init__(self, navn, weapon, armor,ting:list=[]):
        self.navn = navn
        self.maxhp = 100
        self.hp = self.maxhp
        self.weapon = weapon
        self.armor = armor
        self.ting = ting
    
    def damage(self, dmg):#funksjon for spillerskade
        self.hp = self.hp - dmg
    
    def setWeapon(self, pickup):
        self.weapon = pickup
    
    def setArmor(self, pickup):
        self.armor = pickup