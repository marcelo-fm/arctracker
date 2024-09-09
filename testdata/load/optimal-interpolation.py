# Import system modules 
import arcpy from arcpy import * 

#Check out the ArcGIS Image Analyst extension license 
arcpy.CheckOutExtension("ImageAnalyst")  

# Set local variables 
in_background_raster = r"C:\data\global_ssh.tif" 
in_obs_data = r"C:\data\jason_3_ssh.shp" 
obs_field = "SSH" 
background_error_var = 0.1 
obs_error_var = 0.2 
background_error_corr_length = 100 # km 

# Execute 
output = arcpy.ia.OptimalInterpolation(in_background_raster, in_obs_data, obs_field, background_error_var, obs_error_var, background_error_corr_length) 
Output.save(r”c:\output\OI_ssh.crf”)