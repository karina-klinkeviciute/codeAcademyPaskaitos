# API

## Kas tai yra Web API

Web API yra būdas, kuriuo tarp savęs bendrauja skirtingos sistemos ar jų dalys. 
Pavyzdžiui, jei yra tinklalapis, kurio dalis kurta su Python (backend), o dalis su JavaScript(frontend), 
tai šios dvi jo dalys tarpusavyje dažnai bendrauja per Web API (nors ir ne visais atvejais). 

Per Web API šios sistemų dalys vienos kitoms siunčia duomenys. Tai gali būti parieškos rezultatai, kokie nors duomenys, 
kuriuose norim atvaizduoti vartotojui, ar vartotojo įvesti duomenys siunčiami į serverius (pavyzdžiui, komentarai).

Yra keli sutartiniai standartai, kuriais šios Web API įgyvendinami. 

### REST API

Šiuo metu populiariausias standartas yra REST API. REST reiškia REpresentational State Transfer. Tai reiškia, kad 
per ji naudojama duomenų būsenai (state) perduoti ar pakeisti. Paprasčiau tariant, ji naudojama atvaizduoti ar 
keisti duomenis.

#### REST API ir HTTP metodai

Duomenys čia siunčiami naudojant REST HTTP metodus 
(GET - paimti duomenis, ), POST - nusiųsti, DELETE - ištrinti, PUT ir POST - pakeisti. 

#### REST API ir JSON

Naudojant REST API, populiariausias duomenų siuntimo formatas yra JSON. JSON tai tam tikros taisykės, kaip reikia 
struktūriškai sudėlioti duomenis siuntimui į kitą sistemą. JSON formatas labai panašus į Python 
dictionaries ir lists formatą. 

#### REST API struktūra (endpoints)

REST API turi tam tikrą struktūrą. Konkreti struktūra visada priklauso nuo to, kaip API kūrėjai ją suplanuoja. 
Bet yra tam tikri REST API kūrimo principai.

REST API gali būti sudaryta iš daugelio duomenų siuntimo ir gavimo "punktų", angliškai vadinamų "endpoints". 
Kiekvienas endpointas atvaizduoja tam tikrą duomenų klasę, jei įsivaizduotume objektinį programavimą, 
su objektų savybėmis.

Kadangi HTTP metodai nuodojami siųsti duomenis į ir iš API yra "veiksmažodžiai", tai patys "endpointai" būna 
"daiktavardžiai".

Pavyzdžiui, jei turim API, kuri skirta apmokėjimams, galim turėti endpointus "mokėjimas", "mokėtojas", su jų 
savybėmis (duomenimis), panašiai, kaip jei mes turėtume klases "mokėjimas" ir "mokėtojas". 

WEB API pasiekiami per HTTP aresus, panašiai kaip ir interneto puslapiai. 
Jie turi pagrindinį adresą, pavyzdžiui https://www.mokejimai.com Tokiu atveju, mokėjimų ir mokėtojų endpointai 
atrodytų taip: https://www.mokejimai.com/moketojai ir https://www.mokejimai.com/mokejimai

Pasikreipę į šį endpoint, pavyzdžiui įvedę naršyklėje, arba naudodami specialias programas, kaip Postman ar Insomnia, 
arba naudodami Python requests biblioteką, mes galim gauti ir siųsti duomenis iš ir į šias API. 


### REST API naudojimas iš Python

Naudojant Python galima gauti ir siųsti duomenis į įvairias REST API. 

Kadangi REST API yra pasiekiama per žiniatinklio nuorodas, tai galima naudoti biblioteką `requests`, kuri skirta 
užklausoms į internetinius puslapius ar į tuos pačius REST API. 


Su šia biblioteka gauti ir siunčiami duomenys yra koduojami `JSON` formatu, taigi Python'e tam naudojama
`json` biblioteka, kurios pagalba mes gautus ar siunčiamus duomenis galim pakeisti iš Python struktūrų 
į JSON formatą siuntimui, ir atvirkščiai. 

Kai kurios API reikalauja registracijos. T.y., tam, kad galėtume jomis naudoti, reikia užsiregitruoti jų kūrėjų 
tinklalapyje. Dalis jų būna ir mokamos. Jei prie API reikia prisiregistruoti, 
tai jungimuisi prie jos naudojamas API KEY. Tokiu atveju šio API key negalima perkelti į `git` repozitoriją, nes
tada juo gali pasinaudoti kiti žmonės. Tai gali ir kainuoti, ir tapti papildoma saugumo problema. 
Beje, jei jį netyčia įkeliam į git, tada ištrinam ir atnaujinam git repozitoriją, tai nepadeda, nes `git` istoriją
taip pat galima pamatyti. Tada reikia arba trinti visą repozitoriją ir kurti iš naujo, su nauja `git` istorija, 
arba, jei tai įmanoma, gauti naujus API Keys. 

Tam, kad nekelti API į `git`, galima naudoti aplinkos kintamuosius. Nuorodas į informaciją apie juos rasit žemiau. 


## Nuorodos

- Requests  https://github.com/robotautas/kursas/wiki/Requests 

- Json, duomenų eksportavimas į json, paėmimas iš jo https://github.com/robotautas/kursas/wiki/JSON

- API https://github.com/robotautas/kursas/wiki/API's 

- Public API, duomenų paėmimas 

- Aplinkos kintamieji: https://github.com/robotautas/kursas/wiki/Aplinkos-kintamieji 


## (Užduotis:) 

Pasidaryti programėlę, kuri paimtų informaciją iš kokios norsviešos API, ir atvaizduotų jas kokiu nors būdu pas jus.  


## API variantai: 

### API sąrašai: 
- https://rapidapi.com/collection/list-of-free-apis
- https://github.com/public-apis/public-apis


### Kitos: 

- Cat facts: https://alexwohlbruck.github.io/cat-facts/docs/ 

- Dog facts: https://kinduff.github.io/dog-api/

- birds API: https://documenter.getpostman.com/view/664302/S1ENwy59 

- meno kūriniai: https://api.artic.edu/docs/#quick-start 

- emoji: https://github.com/cheatsnake/emojihub 

- https://github.com/robotautas/kursas/wiki/Konsultacija-Oras-pagal-IP


