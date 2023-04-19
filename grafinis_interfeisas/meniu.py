from tkinter import *
from PIL import ImageTk, Image
langas = Tk()
langas.geometry("500x800")

def rodyti_anti():
    antis_foto = ImageTk.PhotoImage(Image.open("antis.jpg"))
    remelis.configure(image=antis_foto)
    remelis.image = antis_foto

def rodyti_sarka():
    sarka_foto = ImageTk.PhotoImage(Image.open("sarka.jpg"))
    remelis.configure(image=sarka_foto)
    remelis.image = sarka_foto

sarka_foto = ImageTk.PhotoImage(Image.open("sarka.jpg"))

remelis = Label(langas, image=sarka_foto)
remelis.pack()

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)


meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="šarka", command=rodyti_sarka)
submeniu.add_command(label="antis", command=rodyti_anti)

submeniu_pirmo = Menu(submeniu, tearoff = 0)
submeniu.add_cascade(label="Trecias", menu=submeniu_pirmo)
submeniu_pirmo.add_command(label="Ketvirtas")

langas.mainloop()
