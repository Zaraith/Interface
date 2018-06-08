import tkinter
from tkinter import *
from math import *

self = Tk()
self.geometry("500x500+500+300")
self['bg']='white'
self.title('Human Walk Analysis')


#Fonctions
def Calculer(event):
	Label4.configure(text='= '+str(eval(Entree.get())))
	


#Table Statistique
self.l = LabelFrame(self, text="Statistics", padx=30, pady=30)
self.l.place(x=15,y=15)

Activate = Checkbutton(self.l, text="Activate")
Activate.grid(column=0, row=0)

Label1 = Label(self.l, text="X =", padx=5,pady=5)
Label1.grid(column=0, row=1)

Label2 = Label(self.l, text="Y =", padx=5,pady=5)
Label2.grid(column=0, row=2)

Label3 = Label(self.l, text="Z =", padx=5,pady=5)
Label3.grid(column=0, row=3)

Calcul = Button(self.l, text="Angle", padx=10,pady=5, command=Calculer)
Calcul.grid(column=0, row=4)

Label4 = Label(self.l, padx=15,pady=15)
Label4.grid(column=2, row=4)

Entree = Entry(self.l, background='white')
Entree.bind("<Return>", Calculer)
Entree.grid(column=1, row=4)



self.mainloop()