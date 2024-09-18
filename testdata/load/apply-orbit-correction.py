# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy
import os
arcpy.CheckOutExtension("ImageAnalyst")

# Set local variables
arcpy.env.workspace = r"C:\Data\SAR\S1"
username = "esaUsername"
password = "esaPassword"
cloud_storage = r"D:\connection_files\eodata.acs" 
folder = r"C:\Data\SAR\Orbits" 

# Execute 
raster_names = arcpy.ListRasters()
for raster_name in raster_names: 
	name, ext = os.path.splitext(raster_name) 
	in_radar = arcpy.Raster(os.path.join(arcpy.env.workspace, raster_name,'manifest.safe'))
	arcpy.ia.DownloadOrbitFile(in_radar, "SENTINEL_PRECISE", username, password, cloud_storage, folder) 
arcpy.ia.ApplyOrbitCorrection(in_radar,"", folder)