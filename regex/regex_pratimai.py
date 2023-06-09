import re

pattern = re.compile(r'\+370\s\d{3}\s\d{5}')

tekstas = "tekstas +370 607 19875 dar tekstas +370 123 65487"

rezultatas = pattern.search(tekstas)

numeris = rezultatas.group()

print(numeris)

print(rezultatas)

def validate_email(input):
    email_regex = re.compile(r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$')
    result = email_regex.search(input)
    if result:
        return True
    return False

print(validate_email('kazkoks@email.lt'))
print(validate_email('neteisingas@@email.lt'))


def split_names(name):
    pattern = re.compile(r'^(?P<kreipinys>[A-Z]\w{1,3}\.)\s([A-Z]\w+)\s([A-Z]\w+)$')
    result = pattern.search(name)
    if result:
        print(f'Visa eilutė: {result.group(0)}')
        print(f'Kreipinys: {result.group("kreipinys")}')
        print(f'Vardas: {result.group(2)}')
        print(f'Pavardė: {result.group(3)}')
        print('----------------------------------')
        print(result.group())
        print((result.groups()))
    else:
        print('Įvestis neatitinka šablono')

split_names('Mr. Clint Eastwood')



card_number = "card1: 0452 6544 0004 4456, card2: 1234 4567 8910 1112"
pattern = re.compile(r'\b(\d{4})\s\d{4}\s\d{4}\s\d{4}\b')
res = pattern.sub('\g<1> **** **** ****', card_number)
print(res)

tekstas = '''Trumpas tekstas 
apie beleką'''
pattern = re.compile(r't\w+', re.IGNORECASE)
res = pattern.findall(tekstas)
print(res)

tekstas = '''Trumpas tekstas 
apie beleką'''

pattern = re.compile(r'^\w+')
res = pattern.findall(tekstas)

pattern2 = re.compile(r'^\w+', re.M)
res2 = pattern2.findall(tekstas)

print(res)
print(res2)

tekstas = 'jonas Jonaitis +370 622 01234'
pattern = re.compile(r'''
                    [A-Z]\w+              # vardas
                    \s                    # tarpas
                    [a-z]\w+              # pavardė
                    \s                    # tarpas
                    \+370\s6\d{2}\s\d{5}  # telefono numeris
                    ''', re.VERBOSE | re.I)
res = pattern.findall(tekstas)
print(res)

