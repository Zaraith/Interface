""" Importation des modules utilisés """
from __future__ import division
import tkinter
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from math import *
from scipy import *
from pylab import *
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from scipy.io import loadmat


class InterfaceGraph_tk(tkinter.Tk): #Classe pour mettre l'appli
	def __init__(self,parent):
		tkinter.Tk.__init__(self,parent) #Constructeur
		""" Afin de référencer le parent """
		self.parent = parent
		""" Afin de séparer le code des éléments créer et la logique du programme """
		self.initialize()

	def initialize(self):
		self.grid()


		""" Création du Menu """
		self.menubar = Menu(self)

		self.menu1 = Menu(self.menubar, tearoff=0)
		self.menu1.add_command(label="Open", command=self.Openfile)
		self.menubar.add_cascade(label="File", menu=self.menu1)

		self.menu2 = Menu(self.menubar, tearoff=0)
		self.menu2.add_command(label="Quit", command=self.alert)
		self.menubar.add_cascade(label="Menu", menu=self.menu2)

		""" Afin de faire fonctionner le menu (affichage du menu) """
		self.config(menu=self.menubar)

	def Openfile(self):
   		filename=askopenfile(title="Choisir le fichier", filetypes=[('TEXT files','.txt')])
   		fichier=open(filename,'r')
   		fichier.read()
   		fichier.close()


	def alert(self):
		if askyesno('Warning', 'Êtes-vous sûr de vouloir faire ça?'):
			showwarning('Warning', 'Aurevoir')
			app.quit()

			
		#Table Statistiques
		self.l = LabelFrame(self, text="Statistics", padx=15, pady=15)
		self.l.place(x=600, y=270, width=280, height=230)

		self.l.Activate = Checkbutton(self.l, text="Activate")
		self.l.Activate.grid(column=0, row=0)

		self.l.Label1 = Label(self.l, text="X =", padx=5,pady=5)
		self.lLabel1.grid(column=0, row=1)

		self.l.Label2 = Label(self.l, text="Y =", padx=5,pady=5)
		self.l.Label2.grid(column=0, row=2)

		self.l.Label3 = Label(self.l, text="Z =", padx=5,pady=5)
		self.l.Label3.grid(column=0, row=3)

		self.l.Label4 = Label(self.l, text="Angle =", padx=15,pady=15)
		self.l.Label4.grid(column=0, row=4)

		self.l.Label5 = Label(self.l, padx=15,pady=15)
		self.l.Label5.grid(column=2, row=4)

		self.l.Entree = Entry(self.l, background='white')
		self.l.Entree.bind("<Return>", self.Calculer)
		self.l.Entree.grid(column=1, row=4)		

	#Fonctions
	def Calculer(event):
		Label5.configure(text='= '+str(eval(Entree.get())))

""" Création du "Main" le premier élément de l'interface/l'application """
if __name__ == "__main__":
    app = InterfaceGraph_tk(None)
    app.title('Human Walk Analysis')
    app.geometry("1000x700+250+20")

    app.mainloop()
