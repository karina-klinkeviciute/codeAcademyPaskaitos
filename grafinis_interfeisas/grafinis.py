from tkinter import Tk, Label, Frame, Button, BOTTOM, LEFT, Y, RIGHT

langas = Tk()


def spausdinti():
    uzrasas["text"] = "aha!"

langas.geometry("500x800")
uzrasas = Label(langas, text="Labas vakaras")

uzrasas.configure(background="blue")

uzrasas.pack()

virsutinis = Frame(langas)
apatinis = Frame(langas)

mygtukas1 = Button(virsutinis, text="1 mygtukas", height=5, width=20, command=spausdinti)
mygtukas1.pack(side=LEFT)

mygtukas2 = Button(virsutinis, text="2 mygtukas", bg='blue', fg="white")
mygtukas2.pack(side=LEFT)

mygtukas3 = Button(apatinis, text="3 mygtukas",  bg='#ffb3fe')
mygtukas4 = Button(apatinis, text="4 mygtukas", activebackground="red")
virsutinis.pack()





apatinis.pack(side=BOTTOM)


mygtukas3.pack(side=RIGHT)
mygtukas4.pack(side=BOTTOM, fill=Y)

rezultato_langelis = Label(langas, text="")

langas.mainloop()
