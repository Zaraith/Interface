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


app = Tk(None)
app.geometry("1000x700+500+300")
app['bg']='white'
app.title('Human Walk Analysis')

#-------------------------------------------------------------------------------

""" Déclaration des fonctions """
def Openfile():
   filename=askopenfile(title="Choisir le fichier", filetypes=[('TEXT files','.txt')])
   fichier=open(filename,'r')
   fichier.read()
   fichier.close()


def alert():
	if askyesno('Warning', 'Êtes-vous sûr de vouloir faire ça?'):
		showwarning('Warning', 'Aurevoir')
		app.quit()


""" Création du Menu """
menubar = Menu(app)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Open", command=Openfile)
menubar.add_cascade(label="File", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Quit", command=alert)
menubar.add_cascade(label="Menu", menu=menu2)

""" Afin de faire fonctionner le menu (affichage du menu) """
app.config(menu=menubar)

#----------------------------------------------------------------------------

#Fonctions
def Calculer(event):
	Label5.configure(text='= '+str(eval(Entree.get())))
	

#Table Statistique
app.l = LabelFrame(app, text="Statistics", padx=15, pady=15)
app.l.place(x=600, y=270, width=280, height=230)

Activate = Checkbutton(app.l, text="Activate")
Activate.grid(column=0, row=0)

Label1 = Label(app.l, text="X =", padx=5,pady=5)
Label1.grid(column=0, row=1)

Label2 = Label(app.l, text="Y =", padx=5,pady=5)
Label2.grid(column=0, row=2)

Label3 = Label(app.l, text="Z =", padx=5,pady=5)
Label3.grid(column=0, row=3)

Label4 = Label(app.l, text="Angle =", padx=15,pady=15)
Label4.grid(column=0, row=4)

Label5 = Label(app.l, padx=15,pady=15)
Label5.grid(column=2, row=4)

Entree = Entry(app.l, background='white')
Entree.bind("<Return>", Calculer)
Entree.grid(column=1, row=4)

#----------------------------------------------------------------------------

# Je mets le lien du fichier de données afin de créer 
# ma courbe. Graphique 2D
M = np.loadtxt('plot_data_file.txt')
plt.plot(M[:,0], M[:,1], 'x', label='Movement')


title('Human Walk Analysis')           


# Limites de l'axe des abscisses
plt.xlim(0, 10) 
# Label de l'axe des abscisses                                  
plt.xlabel('Temps (s)')           


# Limites de l'axe des ordonnées
plt.ylim(-10, 10)
# Label de l'axe des ordonnées                                    
plt.ylabel('Position (ms)')            

#-------------------------------------------------------------------------

# Préparer la figure 3D
fig = plt.figure()
ax = fig.gca(projection='3d')
M = loadtxt('plot_data_file.txt')
plt.plot(M[:,0], M[:,1], 'x')

# Faire les limites de chaques axes
ax.set_xlim((-100, 100))
ax.set_ylim((-100, 100))
ax.set_zlim((-100, 100))

 
# Label de l'axe x                                 
plt.xlabel('Temps (s)')           

# Label de l'axe y                                   
plt.ylabel('Position (ms)') 

# Appel de la légende
legend()
title('Human Walk Analysis')                                       

plt.show()


app.mainloop()