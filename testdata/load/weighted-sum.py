# Name: WeightedSum_Ex_02.py
# Description: Overlays several rasters multiplying each by their given
#    weight and summing them together.

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

wstable = "c:\\test\\Clip_dem.tif VALUE 50;c:\\test\\Clip_aspect.tif VALUE 50"

# Execute WeightedSum
outWeightedSum = WeightedSum(wstable)

# Save the output 
outWeightedSum.save("C:/iapyexamples/output/weightsumout")