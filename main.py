#dette er hovedfilen til spillet, alle python filer blir importert hit.
import python.spiller as player
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
    input("Du møter fiende " +  motstander.navn)
    while(spiller.hp > 0):
        print("Du har ")
        #turen til spilleren er interaktiv, fiende er generert
        ch = SpillerValg("Hva vil du gjøre?? \n 0. angrip med våpenet ditt \n 1. angrip deg selv med våpenet ditt \nskriv alternativ> ", 2)
        if ch == 0:
            motstander.fiende_damage(spiller.weapon.attack)
            print("Du angriper med våpenet ditt og gjør", spiller.weapon.attack, "skade!")
            if(motstander.hp < 1):
                print("Du vant!")
                nyttvåpen = item.generateWeapon(ilvl = romnummer)
                print("Fienden slapp et nytt våpen:", nyttvåpen.name, "med", nyttvåpen.attack, "attack")
                print("Vil du bytte våpen?")
                ch = SpillerValg("0. Ja\n1. Nei\n> ", 2)
                if ch == 0:
                    spiller.weapon = nyttvåpen
                    print("Du byttet våpen!")
                else:
                    print("Du beholdt ditt gamle våpen (taper)")
                break
        elif ch == 1:
            spiller.damage(spiller.weapon.attack)
            print("Du angrep deg selv!")

        print(f'{motstander.navn} angriper med våpenet sitt!')
        spiller.damage(spiller.weapon.attack)
        input()#ended av en runde


#"Gå inn i nytt rom?" -> møtes fiende. Ta i turer på å slå eller lignende? Basert på rommets innhold
#legg in verdier