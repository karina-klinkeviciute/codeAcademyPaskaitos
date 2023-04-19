import random
from tkinter import *

langas = Tk()
langas.title("mano programa")

def spausdinti():
    ivestas_tekstas = laukelis1.get()
    uzrasas["text"] = ivestas_tekstas

langas.geometry("500x800")
uzrasas = Label(langas, text="Labas vakaras")


boksas = Listbox(langas)
sarasas = range(1, 200)
boksas.insert(END, *sarasas)
# boksas.pack(side=LEFT)

# scrollbaras.config(command=langas.yview)

mygtukas1 = Button(langas, text="1 mygtukas", height=2, width=7, command=spausdinti)
laukelis1 = Entry(langas)

uzrasas.grid(row=0, columnspan=5)
laukelis1.grid(row=1, column=0)
mygtukas1.grid(row=2, column=2)
for x in range(10):
    for y in range(10):
        langelis = Label(langas)
        langelis.grid(row=y, column=x)



meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Pirmas")
submeniu.add_command(label="Antras", command=spausdinti)

submeniu_pirmo = Menu(submeniu, tearoff = 0)
submeniu.add_cascade(label="Meniu", menu=submeniu_pirmo)
submeniu_pirmo.add_command(label="Trecias")


def nusokti(event):
    # if mygtukas1.
    skaicius1 = random.randint(0, 9)
    skaicius2 = random.randint(0, 9)
    mygtukas1.grid(row=skaicius1, column=skaicius2)


mygtukas1.bind("<Enter>", nusokti)

langas.mainloop()
