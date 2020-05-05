# script to turn w outputs into netcdf
import os
import numpy as np
import datetime
from netCDF4 import Dataset

num_lat = 80
num_lon = 27
levels = 30
dates = 1356
z_step = 10 
#path to w files (created by fortran code)
w_path = '/Users/brownscholar/Desktop/fortran_files/omega/w/'
#creates file name from date_list
date_list = open('date_list.txt','r')
#creates blank array to fill
w_array = np.zeros((dates,num_lat,num_lon,levels))

for d in range(0,dates): #loops through number of dates
	date = date_list.readline()
	filename = date[:-1]+"_ww.gr"  
	print(filename)
	w_file = open(w_path+filename,"r") #opens w file
	w_file.readline() 
	w_file.readline()
	for i in range(0,levels): 
		for j in range(0,num_lat): 
			for k in range(0,num_lon): 
				w = w_file.readline() 
				w_array[d,j,k,i] = float(w)
	
latitude_val = np.arange(19.625+.5,39.375-.25,0.25)  #creates numpy array with all of the latitude values
longitude_val = np.arange(293.875+.5,300.375-.25,0.25)
time_val = np.arange(377064,604704+168,168)

# opens netcdf file
grp = Dataset('/Users/brownscholar/Desktop/fortran_files/omega.nc','w', format='NETCDF4')
#creates dimensions in netcdf file
grp.createDimension('lon', num_lon-4)
grp.createDimension('lat', num_lat-4)
grp.createDimension('depth', levels) 
grp.createDimension('time', dates)
#creates variables in numpy array 
#f4 means that the values will be floats
longitude = grp.createVariable('longitude', 'f4', 'lon') 
latitude = grp.createVariable('latitude', 'f4', 'lat')  
depth = grp.createVariable('depth', 'f4', 'depth')
time = grp.createVariable('time','f4', 'time')
w = grp.createVariable('w', 'f4', ('time', 'lat', 'lon', 'depth'))

 #fills the variables in the netcdf file with the values from the numpy arrays
longitude[:] = longitude_val  #loops through longitude
latitude[:] = latitude_val  #loops through latitude
time[:] = time_val
depth_arr = (-1)*np.arange(z_step,(levels+1)*z_step,z_step)
depth[:]= depth_arr  #loops through depth

w[:] = w_array[:,2:78,2:25,:]  # takes value from w file and puts it into numpy array

#adds units to netcdf variables
time.units = 'hours since 1950-01-01'
latitude.units = 'degrees_north'
depth.units = 'm'
depth.positive ='down'
depth.axis = 'Z'

w.units = 'm/day'

#closes netcdf file
grp.close()



