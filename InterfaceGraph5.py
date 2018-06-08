from __future__ import division
from scipy import *
from pylab import *

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


# Appel de la légende
legend()                                       

plt.show()