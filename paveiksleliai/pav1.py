from PIL import Image

# im = Image.open("./../grafinis_interfeisas/antis.jpg")

easter = Image.open("nuotraukos/easter.png")
# easter.show()

rabbit = Image.open("nuotraukos/rabbit.jpg")
# rabbit.show()

atvirute = rabbit
atvirute.save("atvirute.jpg")

print(rabbit.format, rabbit.size, rabbit.mode)

print(easter.format, easter.size, easter.mode)

size = 128, 128

# rabbit.thumbnail(size)
# rabbit.show()

box = (150, 150, 300, 300)
dalis = rabbit.crop(box)

# dalis.show()

# apverstas = rabbit.transpose(Image.FLIP_TOP_BOTTOM)
#
# apverstas.show()

# pakeistas = rabbit.resize((100, 600))

# pakeistas.show()

easter.thumbnail((200, 200))

easter_location = (440, 40, easter.size[0]+440, easter.size[1]+40)

rabbit.paste(easter, easter_location, easter)

rabbit.show()

rabbit.save("atvirute.jpg")
