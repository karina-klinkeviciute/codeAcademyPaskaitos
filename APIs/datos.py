import datetime
from time import sleep

import requests

data = datetime.date(year=2022, month=4, day=25)

for i in range(361):

    # suformuojam užklausą konkrečiai datai
    datos_eilute = data.strftime("%Y-%m-%d")
    uzklausa = "https://api.meteo.lt/v1/stations/vilniaus-ams/observations/" + datos_eilute

    # paimam duomenis iš API pagal aukščiau suformuotą eilutę (bus konkrečios dienos duomenys)
    duomenys = requests.get(uzklausa)

    # padidinam datą viena diena, kad kitam cikle imtume kitą dieną
    data = data + datetime.timedelta(days=1)

