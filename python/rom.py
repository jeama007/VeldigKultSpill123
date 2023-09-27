

class Rom:

    # Lager en konstuktør som tar inn roomnumber, trap og quiz. Quiz tenkte jeg kunne være spørsmål man får når man går inn i et nytt rom
    def __init__(self,roomnumber, trap, spørsmål):
        self.roomnumber = roomnumber
        self.trap = trap
        self.spørsmål = spørsmål
    
    def __str__(self):
        print(f"{self.spørsmål}")

    def __repr__(self):
        return f"{self.roomnumber}"


class Quiz:

    # Lager en konstruktør som tar inn respons og kategori. Respons er responsen man får etter man har svart, og kategori er kategorien til spørsmålet
    def __init__(self, respons, kategori):
        self.respons = respons
        self.kategori = kategori




