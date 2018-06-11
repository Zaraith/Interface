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
	Label9.configure(text='= '+str(eval(Entree.get())))
	

#Table Statistique
app.l = LabelFrame(app, text="Statistics", padx=15, pady=15)
app.l.place(x=600, y=200, width=350, height=400)

Activate = Checkbutton(app.l, text="Activate")
Activate.grid(column=0, row=0)

Label1 = Label(app.l, text="X =", padx=5,pady=5)
Label1.grid(column=0, row=1)

Label2 = Label(app.l, text="Y =", padx=5,pady=5)
Label2.grid(column=0, row=2)

Label3 = Label(app.l, text="Z =", padx=5,pady=5)
Label3.grid(column=0, row=3)

Label4 = Label(app.l, text="Min =", padx=15,pady=15)
Label4.grid(column=0, row=4)

Label5 = Label(app.l, text="Max =", padx=15,pady=15)
Label5.grid(column=0, row=5)

Label6 = Label(app.l, text="Moyenne =", padx=15,pady=15)
Label6.grid(column=0, row=6)

Label7 = Label(app.l, text="SD =", padx=15,pady=15)
Label7.grid(column=0, row=7)

Label8 = Label(app.l, text="Angle =", padx=15,pady=15)
Label8.grid(column=0, row=8)

Label9 = Label(app.l, padx=15,pady=15)
Label9.grid(column=4, row=8)

Entree = Entry(app.l, background='white')
Entree.bind("<Return>", Calculer)
Entree.grid(column=3, row=8)

#----------------------------------------------------------------------------

# Je mets le lien du fichier de données afin de créer 
# ma courbe. Graphique 2D
M = np.loadtxt('C:/Users/anzou/Documents/CoursM1/Python/Git/AlexandreDataWalkGraph/Sujet 01/Marker/staticnoise 29052018_001_2018_5_29 Marker30.txt')
plt.plot(M[:,0], M[:,1], 'x', label='Movement')


title('Human Walk Analysis')           


# Limites de l'axe des abscisses
plt.xlim(-4950, -4960) 
# Label de l'axe des abscisses                                  
plt.xlabel('Temps (s)')           


# Limites de l'axe des ordonnées
plt.ylim(953.5, 956)
# Label de l'axe des ordonnées                                    
plt.ylabel('Position (ms)')            

#-------------------------------------------------------------------------

# Préparer la figure 3D
fig = plt.figure()
ax = fig.gca(projection='3d')
M = loadtxt('C:/Users/anzou/Documents/CoursM1/Python/Git/AlexandreDataWalkGraph/Sujet 01/Marker/staticnoise 29052018_001_2018_5_29 Marker30.txt')
plt.plot(M[:,0], M[:,1], 'x')

# Faire les limites de chaques axes
ax.set_xlim((-4950, -4960))
ax.set_ylim((950, 960))
ax.set_zlim((-1, 1))

 
# Label de l'axe x                                 
plt.xlabel('Temps (s)')           

# Label de l'axe y                                   
plt.ylabel('Position (ms)') 

# Appel de la légende
legend()
title('Human Walk Analysis')                                       

plt.show()


app.mainloop()