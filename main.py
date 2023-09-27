#dette er hovedfilen til spillet, alle python filer blir importert hit.
import python.spiller as player
import python.rom as rom
import python.fiende as fiende
import python.item as item

print("Velkommen til veldig kult spill 123!")
romnummer = 1
romliste = []#rommene i rekkefølge i liste
spiller = player.spiller(input("Hva er navnet ditt?> "),item.generateWeapon(ilvl = romnummer),item.generateArmor(ilvl = romnummer),)#lager spilleren med tilfeldige våpen

def SpillerValg(valg, hvormangevalg):
    try:
        choice = int(input(valg))
        if choice < 0 or choice > hvormangevalg:#Midlertidlig
            print("Skriv et gylid tall!!")
            SpillerValg(valg, hvormangevalg)
        return choice
    except:
        print("Skriv et gylid tall!!")
        SpillerValg(valg, hvormangevalg)



while(True):
    '''romliste.append(rom.Rom())
    currentRoom = romliste[romnummer-1]
    romnummer = romnummer + 1
    print(currentRoom)'''
    motstander = fiende.nyFiende(romnummer)
    input("Du møter fiende.", motstander.navn)
    while(spiller.hp > 0):
        #turen til spilleren er interaktiv, fiende er generert
        ch = SpillerValg("Hva vil du gjøre?? \n 0. angrip med våpenet ditt \n 1. angrip deg selv med våpenet ditt \nskriv alternativ> ")
        if ch == 0:
            motstander.damage(spiller.weapon.attack)
            if(motstander.hp < 1):
                print("Du vant!")
                #få våpen til monster her?
                break
        elif ch == 1:
            spiller.damage(spiller.weapon.attack)
        #spillervalg ferdig

        print(f'{motstander.navn} angriper med våpenet sitt!')
        spiller.damage(spiller.weapon.attack)
        input()


#"Gå inn i nytt rom?" -> møtes fiende. Ta i turer på å slå eller lignende? Basert på rommets innhold