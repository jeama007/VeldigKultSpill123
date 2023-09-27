

class Rom:

    # Lager en konstuktør som tar inn roomnumber, trap og quiz. Quiz tenkte jeg kunne være spørsmål man får når man går inn i et nytt rom
    def __init__(self,roomnumber, trap, spørsmål):
        self.roomnumber = roomnumber
        self.trap = trap
        self.spørsmål = spørsmål
    

class Quiz:

    def __init__(self, respons, kategori):
        self.respons = respons
        self.kategori = kategori


