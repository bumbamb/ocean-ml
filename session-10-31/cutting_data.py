from netCDF4 import Dataset
import numpy.ma as ma

# import the netcdf file using Dataset
data = Dataset(r"ssh_1572470095877.nc")
# read in and create variable for lat:
lat = data["latitude"]
# lon:
lon = data["longitude"]

# adt:
adt = data["adt"]

# print shape of the adt variable:
print(adt.shape)
print(lat.shape)
print(lon.shape)
print(lat[:])

# you will need this:
BATS_lat_max = 39.453
BATS_lon_max = 360 -59.648999999999994 # converting from degrees west to degrees east
BATS_lat_min = 19.663 
BATS_lon_min = 360 -66.211 #same

print(BATS_lat_min, BATS_lat_max)
latindex = set()
index = 0
for i in lat:
	if i >BATS_lat_min and i< BATS_lat_max:
		latindex.add(index)
	index += 1
#print(latindex)

lonindex = set()
indexlon = 0
for i in lon:
	if i >BATS_lon_min and i< BATS_lon_max:
		lonindex.add(indexlon)
	indexlon += 1

latmin = min(latindex)
latmax = max(latindex)
lonmin = min(lonindex)
lonmax= max(lonindex)

BATSadt = adt[:, latmin: latmax, lonmin :lonmax]
print(BATSadt.shape)
