import random as r

class Rom:

    # Lager en konstuktør som tar inn roomnumber, trap og quiz. Quiz tenkte jeg kunne være spørsmål man får når man går inn i et nytt rom
    def __init__(self,roomnumber:int=0, roomname:str="det grusomme plaster"):
        self.roomnumber = roomnumber
        self.roomname = roomname


    def get_room(self):
        print("Romnummer er: ", rom1.roomnumber)
        print("")

rom1 = Rom(1, "barbieland")
rom1.get_room()

""" 
def spørSpørsmål(roomnumber):
    if ro
    n = r.randint(1,40)
    print(femteklasse_spørsmål[n]["spørsmål"])
 """

class Quiz:

    # Lager en konstruktør som tar inn respons og kategori. Respons er responsen man får etter man har svart, og kategori er kategorien til spørsmålet
    def __init__(self, spørsmål:str="", svar:str=""):
        self.spørsmål = spørsmål
        self.svar = svar

femteklasse_spørsmål = Quiz()

#En funksjon som velger et tilfeldig spørsmål
def generateQuiz():
    print(r.choice(femteklasse_spørsmål))
    i = r.randint(0, len(Rom.roomnumber))
    


femteklasse_spørsmål = [
    {"spørsmål": "Hva er hovedstaden i Norge?", "svar": "Oslo"},
    {"spørsmål": "Hva er 7 + 3?", "svar": "10"},
    {"spørsmål": "Hva er hovedfargen på en banan?", "svar": "Gul"},
    {"spørsmål": "Hva er verdens største planet?", "svar": "Jupiter"},
    {"spørsmål": "Hva heter den store veggen som ble bygd i Kina for lenge siden?", "svar": "Den kinesiske mur"},
    {"spørsmål": "Hva er hovedstaden i Frankrike?", "svar": "Paris"},
    {"spørsmål": "Hva er hovedfargen på gress?", "svar": "Grønn"},
    {"spørsmål": "Hva er 5 multiplisert med 4?", "svar": "20"},
    {"spørsmål": "Hva er hovedfargen på en eple?", "svar": "Rød"},
    {"spørsmål": "Hva er 9 delt på 3?", "svar": "3"}
]

allmennskunnskap_spørsmål = [
    {"spørsmål":"Hva er en persimon?", "svar": "Frukt"},
    {"spørsmål":"Hva er den største byen i Norge", "svar": "Trondheim"},
    {"spørsmål":"Hva er hovedstaten i Canada?", "svar": "Ottawa"},
    {"spørsmål":"Hvor kommer makronen originalt fra?", "svar": "Italia"},
    {"spørsmål":"Hvor høyt er Galdhøpiggen","svar":"2469 meter"},
    {"spørsmål":"Hvor høyt er Eiffel tårnet?","svar":"324 meter"},
    {"spørsmål":"Fleip eller Fakta: En kvinnelig hest kalles for ei hoppe","svar":"Fakta"},
    {"spørsmål":"Fleip eller Fakta: Joe Biden ble president 12. januar","svar":"Fleip"},
    {"spørsmål":"Fleip eller Fakta: Falsk kantarell er en spiselig matsopp","svar":"Fleip"},
    {"spørsmål":"Fleip eller Fakta: Armstrong er det første mennesket i verdensrommet","svar":"Fleip"}
]


got_spørsmål = [
    {"spørsmål": "Who was responsible for the creation of the Night King?", "alternativer": ["The Lord of Light", "The Children of the Forest", "The Drowned God ", "The First Men "], "svar": "The Children of the Forest"},
    {"spørsmål": "In the TV show, what was Hodor called before he got his tragic door-holding nickname?", "alternativer": ["Wylis", "Horys", "Myrys", "Gladys"], "svar": "Wylis"},
    {"spørsmål": "Dany’s dragons are (or were) called Drogon, Viserion and ____?", "alternativer": ["Dougal", "Vhagar", "Rhaegal", "Balerion"], "svar": "Rhaegal"},
    {"spørsmål": "Who said: 'I don’t plan on knitting by the fire while men fight for me'?", "alternativer": ["Lyanna Mormont", "Sansa Stark", "Ser Brienne of Tarth", "Olenna Tyrell"], "svar": "Lyanna Mormont"}
]
print(got_spørsmål)