import tkinter
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

self = Tk()
self.geometry("500x400+350+400")
self.title('Human Walk Analysis')



""" Déclaration des fonctions """
def Openfile():
   filename=askopenfile(title="Choisir le fichier", filetypes=[('MAT files','.mat')])
   fichier=open(filename,'r')
   fichier.read()
   fichier.close()


def alert():
	if askyesno('Warning', 'Êtes-vous sûr de vouloir faire ça?'):
		showwarning('Warning', 'Aurevoir')
		self.quit()


""" Création du Menu """
menubar = Menu(self)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Open", command=Openfile)
menubar.add_cascade(label="File", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Quit", command=alert)
menubar.add_cascade(label="Menu", menu=menu2)

""" Afin de faire fonctionner le menu (affichage du menu) """
self.config(menu=menubar)


self.mainloop()







