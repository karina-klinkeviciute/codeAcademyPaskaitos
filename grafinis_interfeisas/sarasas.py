from tkinter import *

langas = Tk()
sarasas = range(1, 200)
scrollbaras = Scrollbar(langas)
boksas = Listbox(langas)
scrollbaras.config(command=boksas.yview)
boksas.insert(END, *sarasas)
scrollbaras.pack(side=RIGHT, fill=Y)

boksas.pack(side=LEFT)
langas.mainloop()

