import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from netCDF4 import Dataset
import numpy as np

dataset = Dataset(r/'/Users/brownscholar/Desktop/fortran_files/omega.nc')

w = dataset['w']

#depth = 0
#latitude = 20.125

w_lat = w[:, 0, :, 0]
w_lat = np.swapaxes(w_lat,0,1)
print(w_lat.shape)
plt.pcolormesh(w_lat, cmap = None)
plt.show()