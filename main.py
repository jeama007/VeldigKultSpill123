#dette er hovedfilen til spillet, alle python filer blir importert hit.
import python.spiller as player
import python.rom as rom
import python.fiende as fiende
import python.item as item

print("Velkommen til veldig kult spill 123!")
spiller = player.spiller(input("Hva er navnet ditt?> "),item.generateWeapon(),item.generateArmor())#lager spilleren med tilfeldige våpen

while(True):
    input("AAAAAAAH> ")
    pass

#"Gå inn i nytt rom?" -> møte fiende. Ta i turer på å slå eller lignende? Basert på rommets innhold