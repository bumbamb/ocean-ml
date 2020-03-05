

from netCDF4 import Dataset
import numpy as np
import seawater as sw

dataset = Dataset(r'/Users/brownscholar/Desktop/Internships/Climate/dataset-armor-3d-rep-weekly_1574699840388.nc')

pressure= dataset['depth']
salinity = dataset['so']
temp = dataset['to']
longitude = dataset['longitude']



#print(temp.shape)
##print(salinity.shape)
#print(pressure.shape)
pressure_3d = np.zeros((31, 80, 27))

first_layer= np.repeat(10, 80*27).reshape(80,27)
second_layer = np.repeat(20, 80*27).reshape(80,27)

# layer = []
# for i in pressure[:]:
# 	b = np.repeat(i,80*27).reshape(80,27)
# 	print(b)

for i in range(0,31):
	pressure_3d[i, :,:]= (np.repeat(pressure[i],80*27).reshape(80,27))


density= sw.dens(salinity[:], temp[:], pressure_3d)
density + density -1000
print(density.shape)

time1 = density[0,:,:,:]

# for i in range(0,31):
# 	for j in range(0,80):
# 		for k in range(0,27):
# 			time1[i,j,k]

density_file = open('density_file.txt',"w")
for i in range(0,31):
	for j in range(0,80):
		for k in range(0,27):
			density_file.write(str(time1[i,j,k]))
density_file.close()
