from copy import copy
from time import sleep

from PIL import Image


# ------------ klases aprasymas -------------------
class Automobilis:

    def __init__(self):
        self.zemelapio_failas = "map.jpg"
        self.zemelapis = Image.open(self.zemelapio_failas)
        self.paveiksliukas = copy(self.zemelapis)
        self.auto = Image.open("car.png")
        self.auto.thumbnail((40, 40))
        self.auto = self.auto.transpose(Image.ROTATE_270)
        self.auto_location = (0, 0, self.auto.size[0], self.auto.size[1])
        self.kryptis = 0
        self.x = 0
        self.y = 0

    def pasisukti(self, laipsniai):
        """
        :param laipsniai: gali būti 90, 180 arba 270 laipsnių
        """
        self.kryptis = (self.kryptis + laipsniai) % 360

        if laipsniai == 90:
            self.auto = self.auto.transpose(Image.ROTATE_90)
        if laipsniai == 180:
            self.auto = self.auto.transpose(Image.ROTATE_180)
        if laipsniai == 270:
            self.auto = self.auto.transpose(Image.ROTATE_270)
        self.auto_location = self.auto_location = (self.x, self.y, self.x + self.auto.size[0], self.y + self.auto.size[1])

    def kairen(self):
        self.pasisukti(90)

    def desinen(self):
        self.pasisukti(270)

    def pavaziuoti(self, km):
        if self.kryptis == 0:
            self.y = self.y - km
        elif self.kryptis == 90:
            self.x = self.x - km
        elif self.kryptis == 270:
            self.x = self.x + km
        elif self.kryptis == 180:
            self.y = self.y + km

        self.auto_location = (self.x, self.y, self.x + self.auto.size[0], self.y + self.auto.size[1])

    def parodyti(self):
        self.paveiksliukas = copy(self.zemelapis)
        self.paveiksliukas.paste(self.auto, self.auto_location)
        self.paveiksliukas.show()


# -----------------------klases naudojimas--------------------------------

masinos = []


masina = Automobilis()

masina.desinen()


masina.parodyti()
masinos.append(copy(masina))
sleep(1)

masina.pavaziuoti(200)


masina.parodyti()
masinos.append(copy(masina))
sleep(1)

masina.desinen()


masina.parodyti()
masinos.append(copy(masina))
sleep(1)

masina.pavaziuoti(60)


masina.parodyti()
masinos.append(copy(masina))
sleep(1)

masina.kairen()


masina.parodyti()
masinos.append(copy(masina))
sleep(1)

masina.pavaziuoti(200)

masina.parodyti()
masinos.append(copy(masina))

sleep(1)

masina.parodyti()


paveiksleliai = []
for masina in masinos:
    paveiksleliai.append(masina.paveiksliukas)

paveiksleliai[0].save('vaziuojam.gif', format='GIF', append_images=paveiksleliai[1:], save_all=True, duration=1000, loop=0)

