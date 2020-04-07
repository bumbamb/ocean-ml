

import numpy as np
import tricubic 
def interp(startgrid):
	num_depths = 30 # to avoid problems with seafloor depth
	z_step = 10 
	depth_list = [10, 20, 30, 50, 75, 100, 125, 150, 200, 250, 300, 400]

	new_depth = np.arange(z_step,(num_depths+1)*z_step,z_step) 
	new_depth_index = []
	left = 0
	right = 1
	for i in range(0,len(new_depth)):
		target_value = new_depth[i]
		if target_value > depth_list[right]:
			right += 1
			left +=1
		left_value = depth_list[left]
		right_value = depth_list[right]
		a = target_value-left_value
		b = right_value-left_value
		new_index = a/b+left
		new_depth_index.append(new_index)
		#start grid is shape lat,lon,depth
		lat = startgrid.shape[1]
		lon = startgrid.shape[2]
		depth = startgrid.shape[0]

	interp_grid = np.zeros((len(new_depth_index),lat,lon))
	ip = tricubic.tricubic(list(startgrid),[depth,lat,lon])

	for i in range(0,lat):
		for j in range(0,lon):
			for k in range(0,len(new_depth_index)):
				res = ip.ip([new_depth_index[k],i,j])
				interp_grid[k,i,j] = res

	return interp_grid




from netCDF4 import Dataset
import numpy as np
import seawater as sw
import datetime as td
import tricubic 



dataset = Dataset(r'/Users/brownscholar/Desktop/Internships/Climate/dataset-armor-3d-rep-weekly_1574699840388.nc')

pressure= dataset['depth']
salinity = dataset['so']
temp = dataset['to']
longitude = dataset['longitude']
dynamicheight = dataset['zo']

pressure_3d = np.zeros((31, 80, 27))

first_layer= np.repeat(10, 80*27).reshape(80,27)
second_layer = np.repeat(20, 80*27).reshape(80,27)

# for i in pressure[:]:
# 	b = np.repeat(i,80*27).reshape(80,27)
# 	print(b)

for i in range(0,31):
	pressure_3d[i, :,:]= (np.repeat(pressure[i],80*27).reshape(80,27))

density= sw.dens(salinity[:], temp[:], pressure_3d)
density = density -1000
dynamicheight = dynamicheight[:]*100
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
# density_file = open('density_file.txt','w')
# dataset = Dataset(r'/Users/brownscholar/Desktop/Internships/Climate/dataset-armor-3d-rep-weekly_1574699840388.nc')
time = dataset['time']
#startdate = td.date(1950,1,1)
# for i in range(0,31):
# 	for j in range(0,80):
# 		for k in range(0,27):
# 			density_file.write(str(density_time1[i,j,k])+"\n")
# density_file.close()

#density_file_1 = open("density_file_1", "w")


# for i in range(0,1356):
#     hours = td.timedelta(hours = int(i))
#     eachdate = (startdate+ hours)
#     date= str(eachdate.strftime("%y") + eachdate.strftime("%m") + eachdate.strftime("%d"))
#  	testfile = open("testfile_"+ date + ".txt", "w")
#  	for j in range(0,31):
#  		for k in range(0,80):
#  			for l in range(0,27):
#  				testfile.write(str(density[i,j,k,l])+"\n")
#  	testfile.close()

start_date = td.date(1950,1,1)
#for i in time[:]:
    #hours = td.timedelta(hours = int(i))


#each date
for i in range(0,1356):
	hours = td.timedelta(hours = int(time[i]))#having the hours
	after = start_date + hours
	date = after.strftime("%y") + after.strftime("%m") + after.strftime("%d")
	density_file_1 = open('/Users/brownscholar/Desktop/Data/density/' + date + ".gr","w")
	density_file_1.write("\t30\n\t80\t27\n")
	density_at_time = interp(density[i,:12,:,:])
	interpedheight = interp(dynamicheight[i,:12,:,:])
	interpheightfile = open('/Users/brownscholar/Desktop/Data/dh/' + date + '.gr', 'w')
	interpheightfile.write("\t30\n\t80\t27\n")
	for j in range(0,30):
		for k in range(0,80):
			for l in range(0,27):
				density_file_1.write(str(density_at_time[j,k,l])+'\n')
				interpheightfile.write(str(interpedheight[j,k,l])+'\n')
	density_file_1.close()
	interpheightfile.close()














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
