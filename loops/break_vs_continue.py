
balandzio_temperaturos = [1, 5, -1, 8, 9, 12, 56, 54]

geguzes_temperaturos = [1, 5, 8, 9, 12, -2, 56, 54]


# spausdina ar šalnų buvo
for temperatura in balandzio_temperaturos:
    if temperatura < 0:
        print("šalnų buvo")
        break

# spausdina tik tas dienas, kai šalnų nebuvo
for temperatura in balandzio_temperaturos:
    if temperatura < 0:
        continue
    print("šią dieną šalnų nebuvo")

# spausdina ar salnu buvo
while balandzio_temperaturos:
    temperatura = geguzes_temperaturos.pop()
    if temperatura < 0:
        print("šalnų buvo")
        break

# spausdina tas dienas, kur salnu nebuvo
while balandzio_temperaturos:
    temperatura = balandzio_temperaturos.pop()
    if temperatura < 0:
        continue
    print("šią dieną šalnų nebuvo")