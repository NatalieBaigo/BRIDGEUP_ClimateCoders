#Import packages
import os
from netCDF4 import Dataset
import matplotlib.pyplot as plt
#import sst_anomaly_functions

#Create functions

#Main script
def main():

	
	dataPath = '/Users/brownscholar/Dropbox/BridgeUP_ClimateCoders/Data'
	os.chdir(dataPath)
	data = Dataset('compressed_soda3.12.2_mn_ocean_reg_2011.nc')

	
	lon = data.variables['xt_ocean'][:]
	lat = data.variables['yt_ocean'][:]
	time = data.variables['time'][:]
	depth = data.variables['st_ocean'][:]
	temp = data.variables['temp'][:]
	salt = data.variables['salt'][:]

	
	condition_depth = depth <= 20
	temp_sliced = temp[:,condition_depth,:,:]


	
	temp_mean = temp_sliced.mean()


	temp_anom = temp[:,condition_depth,:,:] - temp_mean
	#temp_anom=(12,2,330,720)
	#print(temp_anom.mean(axis=0).shape)
	temp_anom_yr= temp_anom.mean(axis=0)
	print(temp_anom_yr)
	temp_anom_depth= temp_anom.mean(axis = 0).mean(axis = 0).shape
	print(temp_anom_depth)

	plt.figure()
	plt.title("Contour mapping Of The Sea Floor")
	plt.xlabel("Longitude")
	plt.ylabel("Latitude")
	cm= plt.cm.get_cmap("BuPu")
	plt.contour(lon,lat,temp_anom_yr,cmap= cm)
	ax = plt.contour(lon,lat,temp_anom_yr,colors = 'black')
	plt.colorbar(label='--------->')
	plt.savefig("contour.jpg")
	plt.show()
	

#Execute main script
if __name__ == '__main__':
	main()

