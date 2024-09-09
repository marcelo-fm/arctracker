import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

CreateAccuracyAssessmentPoints("c:\\test\\cls.tif", "c:\\test\\apnt1.shp", 
                               "COMPUTED", "1500", "RANDOM")