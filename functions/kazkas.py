def sarasas(skaiciai):
    nepasikartojantys = []
    for x in skaiciai:
        if x not in nepasikartojantys:
            nepasikartojantys.append(x)
    return nepasikartojantys


aa = [1, 1, 1, 3, 3, 3, 4, 4, 34, 34, 54, 31, 31, 55, 55, 1, 1, 34, 55, 50]
ats_skaiciai = sarasas(aa)
print(ats_skaiciai)

