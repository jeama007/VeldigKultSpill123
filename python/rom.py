import random as r

class Rom:
    # Lager en konstuktør som tar inn romnummer og romnavn
    def __init__(self, romnavn, romnummer:int=1):
        self.romnavn = romnavn
        self.romnummer = romnummer

    def get_rom(self):
        return f"Du har kommet til rom nummer: {self.romnummer}"

romnavnListe = [
    "Kjelleren i S-bygget", 
    "Kiwi",
    "The Red Keep",
    "Fanatisk gudsstue",
    "Dommedagens Brønn",
    "Enchanted Echo Haven",
    "Freddy Fazbear's pizzeria",
    "Peculiar Paradox Parlor",
    "Oddball Oasis Annex",
    "Smultronstället",
    "Regnbueobservatoriet",
    "Vulkankjelleren",
    "Nissen's Bibliotek",
    "Det blå rommet",
    "Mørkets loft"
]

def generateRom(romnavn="", romnummer=1):
    if romnavn == "":
        romnavn = f"{romnavnListe[r.randint(0,14)]}"
    if romnummer == 0:
        romnummer = romnummer + 1
    return Rom(romnavn, romnummer)


kakeRom = Rom("Kake-Rom", 16) #Her er det siste rommet "Kake-rom"
def Kake(): #En funksjon som printer en melding etter at du har vunnet
    print("Gratulerer du er superkul!")
    print("Reisen din er slutt")
    game = False

class Quiz:
    # Lager en konstruktør som tar inn respons og kategori. Respons er responsen man får etter man har svart, og kategori er kategorien til spørsmålet
    def __init__(self, spørsmål:str="", svar:str=""):
        self.spørsmål = spørsmål
        self.svar = svar    
        

class Quiz:
    # Lager en konstruktør som tar inn respons og kategori. Respons er responsen man får etter man har svart, og kategori er kategorien til spørsmålet
    def __init__(self, spørsmål:str="", alternativer=None, svar:str=""):
        self.spørsmål = spørsmål
        self.alternativer = alternativer or []
        self.svar = svar

femteklasse_spørsmål = Quiz()
allmennskunnskap_spørsmål = Quiz()
got_spørsmål = Quiz()

femteklasse_spørsmål = [ #Liste med spørsmål til rommene
    Quiz("Hva er hovedstaden i Norge?", [], "Oslo"),
    Quiz("Hva er 7 + 3?", [], "10"),
    Quiz("Hva er hovedfargen på en banan?", [], "Gul"),
    Quiz("Hva er verdens største planet?", [], "Jupiter"),
    Quiz("Hva heter den store veggen som ble bygd i Kina for lenge siden?", [], "Den kinesiske mur"),
    Quiz("Hva er hovedstaden i Frankrike?", [], "Paris"),
    Quiz("Hva er hovedfargen på gress?", [], "Grønn"),
    Quiz("Hva er 5 multiplisert med 4?", [], "20"),
    Quiz("Hva er hovedfargen på en eple?", [], "Rød"),
    Quiz("Hva er 9 delt på 3?", [], "3")
]

allmennskunnskap_spørsmål = [ #Liste med spørsmål til rommen
    Quiz("Hva er en persimon?", "Frukt"),
    Quiz("Hva er den største byen i Norge", "Trondheim"),
    Quiz("Hva er hovedstaten i Canada?", "Ottawa"),
    Quiz("Hvor kommer makronen originalt fra?", "Italia"),
    Quiz("Hvor høyt er Galdhøpiggen", "2469 meter"),
    Quiz("Hvor høyt er Eiffel tårnet?", "324 meter"),
    Quiz("Fleip eller Fakta: En kvinnelig hest kalles for ei hoppe", "Fakta"),
    Quiz("Fleip eller Fakta: Joe Biden ble president 12. januar", "Fleip"),
    Quiz("Fleip eller Fakta: Falsk kantarell er en spiselig matsopp", "Fleip"),
    Quiz("Fleip eller Fakta: Armstrong er det første mennesket i verdensrommet", "Fleip")
]


got_spørsmål = [ #Liste med spørsmål til rommene
    Quiz("Who was responsible for the creation of the Night King?", ["The Lord of Light", "The Children of the Forest", "The Drowned God ", "The First Men "], "The Children of the Forest"),
    Quiz("In the TV show, what was Hodor called before he got his tragic door-holding nickname?", ["Wylis", "Horys", "Myrys", "Gladys"], "Wylis"),
    Quiz("Dany’s dragons are (or were) called Drogon, Viserion and ____?", ["Dougal", "Vhagar", "Rhaegal", "Balerion"], "Rhaegal"),
    Quiz("Who said: 'I don’t plan on knitting by the fire while men fight for me'?", ["Lyanna Mormont", "Sansa Stark", "Ser Brienne of Tarth", "Olenna Tyrell"], "Lyanna Mormont")
]


# Generer et tilfeldig spørsmål fra en kategori
def generateRandomQuiz(femteklasse, allmennskunnskap, got):
    # Velg en tilfeldig kategori
    kategori = r.choice([femteklasse, allmennskunnskap, got])
    # Velg et tilfeldig spørsmål fra den valgte kategorien
    tilfeldig_spørsmål = r.choice(kategori)
    return tilfeldig_spørsmål

tilfeldig_spørsmål = generateRandomQuiz(femteklasse_spørsmål, allmennskunnskap_spørsmål, got_spørsmål)
