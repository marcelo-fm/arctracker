import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

accuracy_assessment_points = "c:test\\aapnt2.shp"
confusion_matrix = "c:\\test\\confm.dbf"

ComputeConfusionMatrix(accuracy_assessment_points, confusion_matrix)