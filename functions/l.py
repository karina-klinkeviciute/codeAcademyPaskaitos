def kazkas(a):
    return a*2+2

b = kazkas(12)

print(b)

b = lambda a: a*2+2

print(b(12))

sarasas = [2, 5, 4, 65, 78, 99, 38]


sarasas2 = map(kazkas, sarasas)

# print(sarasas2)


sarasas2 = map(lambda a: a*2+2, sarasas)

for skaicius in sarasas2:
    print(skaicius)

