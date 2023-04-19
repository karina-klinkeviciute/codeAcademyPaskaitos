import datetime
from time import sleep, strptime
import locale

from locale import *
locale.setlocale(LC_ALL, '')


def labas_vakaras(vardas):
    print(f"labas vakaras {vardas}")

def ar_keliamieji(data):
    # paprasta funkcija
    if data.year % 4 == 0:
        return True
    return False


ar_sie_metai_keliamieji = ar_keliamieji(datetime.datetime.now())

print(ar_sie_metai_keliamieji)


class Sukaktis:

    def __init__(self, data, pavadinimas):
        """

        :param data: data String formatu (YYYY-mm-dd)
        :param pavadinimas: sukakties pavadinimas
        """
        self.data = datetime.datetime.strptime(data, "%Y-%m-%d")
        self.pavadinimas = pavadinimas

    def ar_keliamieji(self):
        # klasės metodas
        if self.data.year % 4 == 0:
            return True
        return False

    def atimti_dienas(self, dienos):

        nauja_data = "kazkas"

        return nauja_data

    def __str__(self):
        data = self.data.strftime("%Y/%b/%d")
        return f"{self.pavadinimas}: {data}"

    # def kiek_praejo(self, laiko_vienetai):
    #
    #
    #     return kiekis
    #
    # def praejo_metu(self):
    #
    #     return metai
    #
    # def praejo_dienu()
    #
    #     return dienos


siandien = Sukaktis(data="2023-04-14", pavadinimas="šiandien")


ar_sie_metai_keliamieji = siandien.ar_keliamieji()

print(ar_sie_metai_keliamieji)


data1 = Sukaktis("1979-12-15", "Gimtadienis")

data2 = Sukaktis('2000-01-20', "Vestuvės")

mokyklos_baigimas = Sukaktis('1988-06-01', "Mokyklos baigimas")

svarbios_datos = [data1, data2, mokyklos_baigimas]


#
# for data in svarbios_datos:
#     print(data)



# if gimtadienis.ar_keliamieji():
#     print("Gimtadienis buvo keliamaisiais metais")
# else:
#     print("Gimtadienis buvo ne keliamaisiais metais")
#
# sleep(5)
#
# if vestuves.ar_keliamieji():
#     print("Vestuves buvo keliamaisiais metais")

# vestuves.kiek_praejo("dienos")

ivestos_datos = []

# while True:
#     data = input("Iveskite data, formatu YYYY-mm-dd: ")
#     pavadinimas = input("Iveskite pavadinima: ")
#
#     sukaktis = Sukaktis(data, pavadinimas)
#
#     ivestos_datos.append(sukaktis)
#
#     ar_testi = input("Ar testi? (Y/n) ")
#
#     if ar_testi == "n":
#         break


for data in ivestos_datos:
    print(data)
