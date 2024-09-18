# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy 
from arcpy.ia import *
arcpy.CheckOutExtension("ImageAnalyst") 

#Set local variables
in_raster = r'C:\data\input_raster.crf'         
background_value=0        
flood_fill=True     
expand_background=0        
expand_mask=0     
min_region_size=100       
background_nodata=False     
   
#Execute
out_raster = arcpy.ia.CreateBinaryMask(in_raster, background_value, flood_fill, 
				expand_background, expand_mask, min_region_size, 
				background_nodata)

#Save the output
out_raster.save(r'C:\Data\FloodMap\WaterMask.crf')