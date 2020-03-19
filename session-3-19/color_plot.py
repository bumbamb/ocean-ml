import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

w_file = '/path/to/file' #fix this
original_data = #open netcdf file

#get latitude and longitude from netcdf file: 
# here:


num_lat = 80
num_lon = 27
levels = 30

# make empty numpy array of lat, lon depth shape for storing w:
#

# use a loop to read w_file into the variable 
#(skip first two lines of the file)



#this stuff defines the colorspace (we can google colormaps to learn more if we want to)
top = cm.get_cmap('Blues_r', 128)
bottom = cm.get_cmap('Reds', 128)

newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='RedBlue')


#now select one level of the data (surface level):



#and use the following function to plot your data:
#function to make colorplot is:
# p = plt.pcolormesh(V,cmap = newcmp), where V is the numpy array with the data
