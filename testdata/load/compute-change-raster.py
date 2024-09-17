# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")


LandcoverChange = arcpy.ia.ComputeChangeRaster(
	"Landcover_2000.tif", "Landcover_2020.tif", "CATEGORICAL_DIFFERENCE", 
	"'Forest';'Agriculture';'Water';'Barren'", "'Urban'", 
	"CHANGED_PIXELS_ONLY", "AVERAGE")
	
# Save output  
LandcoverChange.save("C:/Data/Landcover_2000_2020.tif")