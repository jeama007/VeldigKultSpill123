#dette er hovedfilen til spillet, alle python filer blir importert hit.
import python.spiller as player
import python.fiende as fiende
import python.item as item
import python.rom as rom

print("Velkommen til veldig kult spill 123!")
romliste = []#rommene i rekkefølge i liste
romnummer = 1 #romliste nummer i guess
spiller = player.spiller(input("Hva er navnet ditt?> "),item.generateWeapon(ilvl = len(romliste)+1),item.generateArmor(ilvl = len(romliste)+1),)#lager spilleren med tilfeldige våpen

def SpillerValg(valg, hvormangevalg):
    if (hvormangevalg == 0):
        print("Det er faktisk ingenting her")
        return -1
    try:
        choice = int(input(valg))
        if choice < 0 or choice > hvormangevalg-1:#Midlertidlig
            print("Skriv et gylid tall!!\n")
            SpillerValg(valg, hvormangevalg)
        return choice
    except:
        print("Skriv et gylid tall!!\n")
        SpillerValg(valg, hvormangevalg)


game = True
while(game):
    #romliste.append(rom.Rom())
    #currentRoom = romliste[romnummer-1]
    romliste.append(rom.generateRom("",len(romliste)))
    print(f"du er på {romliste[len(romliste)-1].romnavn}\n")
    #her kan vi ha skille mellom hva som skjer i rommene. Man møter enten en fiende, en quiz, eller en kake mmmmmmm

    motstander = fiende.nyFiende(len(romliste)+1)
    if input("Du møter fiende " +  motstander.navn) == "quit":
        game = False
    
    while(spiller.hp > 0 and motstander.hp > 0 and game == True):#kamploop
        print("Du har", spiller.hp, "hp igjen.\n",motstander.navn,"har ",motstander.hp,"igjen. \n")
        #turen til spilleren er interaktiv, fiende er generert
        ch = SpillerValg("Hva vil du gjøre?? \n 0. angrip med våpenet ditt \n 1. angrip deg selv med våpenet ditt \n 2. bruk et objekt fra ditt inventar \nskriv alternativ> ", 3)
        if ch == 0:
            motstander.fiende_damage(spiller.weapon.attack)
            print("Du angriper med våpenet ditt og gjør", spiller.weapon.attack, "skade!")
            if(motstander.hp < 1):
                print("Du vant!")
                nyttvåpen = item.generateWeapon(ilvl = len(romliste)+1)
                print("Fienden slapp et nytt våpen:", nyttvåpen.name, "med", nyttvåpen.attack, "attack")
                print("Vil du bytte våpen? \n")
                ch = SpillerValg("0. Ja\n1. Nei\n> ", 2)
                if ch == 0:
                    spiller.weapon = nyttvåpen
                    print("Du byttet våpen!")
                elif ch == 1:
                    print("Du byttet ikke ditt gamle våpen.")

                break
        elif ch == 1:
            spiller.damage(spiller.weapon.attack)
            print("Du angrep deg selv og gjorde",spiller.weapon.attack,"skade!")
        elif ch == 2:
            print("\nher er tingene du har i ryggsekken din: \n")
            for i in range(len(spiller.ting)):
                print(f"{i}. " + spiller.ting[i])
            tingvalg = SpillerValg("\nHvilket objekt vil du bruke?> ", len(spiller.ting))
            if tingvalg == -1:
                print("\nDu stor der veldig kleint og gjorde ingenting.\n")
            elif tingvalg >= 0:
                #her bruker man en item
                print("du brukte",spiller.ting[tingvalg])
                spiller.ting.remove(spiller.ting[tingvalg])
            

        if spiller.hp <= 0:#spiller død
            print("\nDu er  er død :(\n")
            game = False
        if motstander.hp > 0 and spiller.hp > 0:#motstander angrep
            print(f'{motstander.navn} angriper med våpenet sitt og gjør {motstander.damage} skade!')
            spiller.damage(motstander.damage)

        input("\n--press enter to continieute--\n")#pause

print("Game over.")


#"Gå inn i nytt rom?" -> møtes fiende. Ta i turer på å slå eller lignende? Basert på rommets innhold