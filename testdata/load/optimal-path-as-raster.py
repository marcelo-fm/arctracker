# Name: OptimalPathAsRaster_Ex_02.py
# Description: Calculates the least-cost path from a source to 
#              a destination.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inDestination = "observers.shp"
distAccumRaster = "distAccum.tif"
backDir = "backDir2.tif"
destField = "FID"
pathType = "EACH_CELL"

# Execute CostPath
outOptimalRasPath = OptimalPathAsRaster(inDestination, distAccumRaster, backDir, destField,
                       pathType)

# Save the output 
outOptimalRasPath.save("c:/sapyexamples/output/optimalraspath02.tif")