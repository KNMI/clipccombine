# test nomalisation functions
import netCDF4
import numpy as np
import clipc_wp8_norm as cn

url1 =  'http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/tier1_indicators/icclim_cerfacs/TNn/MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1/TNn_OCT_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1_EUR-11_2006-2100.nc'

nc1 = netCDF4.Dataset(url1,'r')

for k1 , v in nc1.variables.iteritems():
# 	if "grid_mapping" in v.ncattrs():
# 		var = k1
	print k1 #,": ", v.standard_name

lats = nc1.variables['lat'][:]
lons = nc1.variables['lon'][:]
#print nc1.variables['TNn'][:].shape

#print  np.min(nc1.variables['lat'][:])
#print  np.max(nc1.variables['lat'][:])
#print  np.mean(nc1.variables['lat'][:])
#print  np.std(nc1.variables['lat'][:])
print ' '
#print  nc1.variables['lat'][411,423]
#print nc1.variables['TNn'][94,:].shape

tnn = nc1.variables['TNn'][0][:] # read var...
nrm = cn.normA(tnn)
nrm2 = cn.normB(tnn)

print tnn.shape
print  np.min(tnn)
print  np.max(tnn)
print  np.mean(tnn)
print  np.std(tnn)

print nrm.shape
print  np.min(nrm)
print  np.max(nrm)
print  np.mean(nrm)
print  np.std(nrm)

print nrm2.shape
print  np.min(nrm2)
print  np.max(nrm2)
print  np.mean(nrm2)
print  np.std(nrm2)

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig = plt.figure(1)

lat_0 = lats.mean()
lon_0 = lons.mean()

#ax = fig.add_subplot("111")
basemap = Basemap(resolution='l',projection='ortho', lat_0=lat_0,lon_0=lon_0) 

data = tnn #nrm2 #nrm
#xi, yi = basemap(*np.meshgrid(lons, lats))	 
xi, yi = basemap(lons, lats)

	# Plot Data
cs = basemap.pcolormesh(xi,yi,np.squeeze(data))

# Add Coastlines, States, and Country Boundaries
basemap.drawcoastlines()
basemap.drawcountries()
basemap.colorbar()

plt.show()
