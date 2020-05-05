from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap



dataset = Dataset(r'/Users/brownscholar/Desktop/fortran_files/omega.nc')

w = dataset['w']
lat = dataset['latitude']
depth = dataset['depth']
longtitude = dataset['longtitude']

title = "hovmoller diagram at latitude " + str(lat[0])
#depth = 0
#latitude = 20.125

w_lat_0 = w[:, 0, :, 0]
w_lat_0 = np.swapaxes(w_lat_0,0,1)
w_lat_1 = w[:,0, :, 1]
w_lat_1= np.swapaxes(w_lat_1,0,1)
w_lat_2 = w[:,0,:,2]
w_lat_2 = np.swapaxes(w_lat_2,0,1)

ax[0].set_yticks(np.arange(0,10,2)) # note you still need this part for the spacing
ax[0].set_yticklabels(myexample)
#print(w_lat.shape)
cmap = cm.get_cmap('bwr')
_min = -10
_max = 10
fig, ax = plt.subplots(3,1)
ax[0].pcolormesh(w_lat_0,cmap=cmap, vmin = _min, vmax = _max)
ax[1].pcolormesh(w_lat_1,cmap=cmap, vmin = _min, vmax = _max)
ax[2].pcolormesh(w_lat_2,cmap=cmap, vmin = _min, vmax = _max)
#ax[0].set_yticks(np.arange(0,10,2)) # note you still need this part for the spacing
#ax[0].set_yticklabels(myexample)
ax[0].set_title("Depth = " + str(depth[0])) 
ax[1].set_title("Depth = " + str(depth[1])) 
ax[2].set_title("Depth = " + str(depth[2])) 
#plt.pcolormesh(w_lat, cmap = cmap)
#plt.title(title)
plt.show()