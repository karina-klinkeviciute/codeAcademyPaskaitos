

def funkcija(kintamasis1, argumentas2):
    '''
    Spausdina x ir a reikšmes
    :param kintamasis1: spausdinama reikšmė
    :param argumentas2: kita spausdinama reikšmė
    :return: skaicius
    '''

    global a
    x = 8
    x = x + 2
    a = a+2
    print(a)
    print(x)
    return x
a = 5

y = funkcija()

print("y: ", y)

funkcija()


















