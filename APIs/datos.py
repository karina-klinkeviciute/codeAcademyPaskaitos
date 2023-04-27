import datetime
from time import sleep

import requests

data = datetime.date(year=2022, month=4, day=25)

for i in range(361):
    datos_eilute = data.strftime("%Y-%m-%d")
    uzklausa = "https://api.meteo.lt/v1/stations/vilniaus-ams/observations/" + datos_eilute

    data = data + datetime.timedelta(days=1)
    print(uzklausa)

    sleep(2)
    # šito čia gal ir nereikia, nes API tikimasi daug užklausų, čia ne web scraping

    duomenys = requests.get(uzklausa)

    print(duomenys.text)
