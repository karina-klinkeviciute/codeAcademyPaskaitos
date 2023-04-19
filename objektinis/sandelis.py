class Sandelis:

    def __init__(self, adresas):
        self.adresas = adresas

    def atidaryti(self):
        self.atidarytas = True

    def uzdaryti(self):
        self.atidarytas = False

    def __str__(self):
        return f"Sandėlis adresu {self.adresas}"

pirmas = Sandelis("Savanoriu 15")
antras = Sandelis("Savanoriu 17")

pirmas.uzdaryti()


print(pirmas)


pajamu_zurnalas = []
