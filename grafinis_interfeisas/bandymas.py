# from tkinter import *
# root = Tk
# root.title("Frame Example")
# root.config(bg="skyblue")
# left_frame = Frame(root, width=200, height=400)
# left_frame.grid(row=0, column=0, padx=10, pady=5)
# root.mainloop()

def aha(kazkas):
    if not hasattr(aha, "contexts"):
        aha.contexts = {}

    aha.contexts[kazkas] = kazkas

    print(aha.contexts)


aha(1)

aha("labas")

aha("nu gerai")

