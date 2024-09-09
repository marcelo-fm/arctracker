import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

UpdateAccuracyAssessmentPoints("c:\\test\\aapnt1.shp", "c:\\test\\grndtru.tif", "c:\\test\\aapnt2.shp", "GROUND_TRUTH")