from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap



dataset = Dataset(r'/Users/brownscholar/Desktop/fortran_files/omega.nc')

w = dataset['w']
lat = dataset['latitude']
title = "hovmoller diagram at latitude " + str(lat[0])
#depth = 0
#latitude = 20.125

w_lat = w[:, 0, :, 0]
w_lat = np.swapaxes(w_lat,0,1)
print(w_lat.shape)
cmap = cm.get_cmap('bwr')

plt.pcolormesh(w_lat, cmap = cmap)
plt.title(title)
plt.show()