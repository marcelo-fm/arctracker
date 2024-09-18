import arcpy 
from arcpy import env 
from arcpy.ia import *

env.workspace = "C:/data" 

outLandCover = ClassifyRaster("Landsat8_Redlands", "LandCover.ecd")

outLandCover.save("RedlandsLandcover")