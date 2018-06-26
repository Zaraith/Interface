from tkinter import Tk, ttk, Label

fenetre = Tk()

l = ttk.LabelFrame(fenetre, text="File Name")
l.pack(fill="y", expand="no")
 
Label(l, text="A l'intérieure de la frame").pack()

l = ttk.LabelFrame(fenetre, text="Titre de la frame")
l.pack(fill="y", expand="no", pady=60)
 
Label(l, text="A l'intérieure de la frame").pack()

fenetre.mainloop()

