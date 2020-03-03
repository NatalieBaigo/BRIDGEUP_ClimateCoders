#Import packages
import os
from netCDF4 import Dataset
import matplotlib.pyplot as plt
<<<<<<< HEAD
#import sst_anomaly_functions
=======
import sst_anomaly_functions
>>>>>>> 6b5fa747cbdf77c3660bfa173fe4f7c49eb59627

#Create functions

#Main script
def main():

<<<<<<< HEAD
	
	dataPath = '/Users/brownscholar/Dropbox/BridgeUP_ClimateCoders/Data'
	os.chdir(dataPath)
	data = Dataset('compressed_soda3.12.2_mn_ocean_reg_2011.nc')

	
=======
	#Navigates to our data folder
	dataPath = '/Users/hellenfellow/Dropbox (AMNH)/BridgeUP_ClimateCoders/Data'
	os.chdir(dataPath)
	data = Dataset('compressed_soda3.12.2_mn_ocean_reg_2017.nc')

	# Setting variables
>>>>>>> 6b5fa747cbdf77c3660bfa173fe4f7c49eb59627
	lon = data.variables['xt_ocean'][:]
	lat = data.variables['yt_ocean'][:]
	time = data.variables['time'][:]
	depth = data.variables['st_ocean'][:]
	temp = data.variables['temp'][:]
	salt = data.variables['salt'][:]

<<<<<<< HEAD
	
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
	
=======
	#Slicing 
	condition_depth = depth <= 20
	temp_sliced = temp[:,condition_depth,:,:]

	#Creates average temperature
	temp_mean = temp_sliced.mean()
	
	#Calculate anomalies
	temp_anom = temp[:,condition_depth,:,:] - temp_mean
	#temp_anom = (12,2,330,720)
	temp_anom_yr = temp_anom.mean(axis = 0)
	print(temp_anom_yr.shape)
>>>>>>> 6b5fa747cbdf77c3660bfa173fe4f7c49eb59627

#Execute main script
if __name__ == '__main__':
	main()
<<<<<<< HEAD

=======
>>>>>>> 6b5fa747cbdf77c3660bfa173fe4f7c49eb59627
