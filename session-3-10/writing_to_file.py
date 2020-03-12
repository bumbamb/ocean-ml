


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

#time1 = density[0,:,:,:]
time1 = density
# for i in range(0,31):
# 	for j in range(0,80):
# 		for k in range(0,27):
# 			time1[i,j,k]

# density_file = open('density_file.txt',"w")
# for i in range(0,31):
# 	for j in range(0,80):
# 		for k in range(0,27):
# 			density_file.write(str(time1[i,j,k]))
# density_file.close()

density_time1 = density[:,:,:]
#print(density_time1)
density_file = open('density_file.txt','w')

# for i in range(0,31):
# 	for j in range(0,80):
# 		for k in range(0,27):
# 			density_file.write(str(density_time1[i,j,k])+"\n")
# density_file.close()

#density_file_1 = open("density_file_1", "w")
print(density.shape)

for i in range(0,1356):
 	testfile = open("testfile_"+str(i)+".txt", "w")
 	for j in range(0,31):
 		for k in range(0,80):
 			for l in range(0,27):
 				testfile.write(str(density[i,j,k,l])+"\n")
 	testfile.close()
















# =======
# from netCDF4 import Dataset
# import numpy as np
# import seawater as sw 

# dataset = Dataset(r'/Users/brownscholar/Desktop/dataset-armor-3d-rep-weekly_1581373134952.nc')

# pressure = dataset['depth']
# temperture = dataset['to']
# salinity = dataset['so']

# print(pressure.shape)
# print(temperture.shape)
# print(salinity.shape)

# pressure_3d = np.zeros((31,80,27))

# # for depth_level in pressure:
# # 	print(np.repeat(depth_level,80*27).reshape((80,27)))


# for i in range(0,31):
# 	#print(np.repeat(pressure[i],80*27).reshape((80,27)))
# 	pressure_3d[i,:,:] = np.repeat(pressure[i],80*27).reshape((80,27))
# 	#print(pressure_3d[i,:,:])

# density = sw.dens(salinity[:],temperture[:],pressure_3d)
# density = density-1000

# print(density.shape)

# for i in range(0,10):
# 	for j in range(0,10):
# 		for k in range(0,10):
# 			print(i,j,k)
# >>>>>>> ae2a66d07524f15dcce27fbe52b54d85ec246ec5
