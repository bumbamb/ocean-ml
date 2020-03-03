#to do
import numpy as np
from netCDF4 import Dataset
dataset = Dataset(r'/Users/brownscholar/Desktop/Internships/Climate/dataset-armor-3d-rep-weekly_1574699840388.nc')

geopotential_height = dataset['zo']
print(geopotential_height)