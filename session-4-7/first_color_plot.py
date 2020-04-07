import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from netCDF4 import Dataset
import numpy as np

# stuff that sets the plotting settings
top = cm.get_cmap('Blues_r', 128)
bottom = cm.get_cmap('Reds', 128)
newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='RedBlue')
_min = -10
_max = 10
#

# facts about our data:
num_lat = 80
num_lon = 27
levels = 30
dates = 1356
z_step = 10 


# 1 - import netcdf file

# 2 - load the w variable

# 3 - get lat x lon numpy array of w_variable (pick a single depth and a single time)


#4 - plot the numpy array you have: 
# once you have this, you can use plt.pcolormesh() to plot it.
# ex: if your numpy array was called my_numpy_array:
# plt.pcolormesh(my_numpy_array,cmap = newcmp,vmin = _min, vmax = _max)
# to add colorbar: 
# plt.colorbar(label = 'm/day')
