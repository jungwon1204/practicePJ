from matplotlib.pyplot import *
import numpy as np
from mpl_toolkits.mplot3d.axes3d import *

x, y = np.meshgrid(np.arange(-1,1,0.1), 
np.arange(-1,1,0.1))

z = x**2 + y**2#피타고라스 

fig = figure()
ax = fig.add_subplot(111, projection = "3d")
ax.scatter(x, y, z, c = z)

show()