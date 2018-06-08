import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from scipy.io import loadmat
from pylab import *


# Préparer la figure 3D
fig = plt.figure()
ax = fig.gca(projection='3d')
M = loadtxt('plot_data_file.txt')
plt.plot(M[:,0], M[:,1], 'x')

# Faire les limites de chaques axes
ax.set_xlim((-100, 100))
ax.set_ylim((-100, 100))
ax.set_zlim((-100, 100))


plt.show()