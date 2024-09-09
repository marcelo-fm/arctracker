# Name: FocalStatistics_Ex_02.py
# Description: Calculates a statistic on a raster over a specified
#    neighborhood.
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "elevation"
neighborhood = NbrRectangle(10, 10, "CELL")

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute FocalStatistics
outFocalStatistics = FocalStatistics(inRaster, neighborhood, "MINORITY",
                                     "")

# Save the output 
outFocalStatistics.save("C:/output/focalstatout")