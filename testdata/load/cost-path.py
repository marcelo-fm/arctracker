# Name: CostPath_Ex_02.py
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
costDistanceRaster = "costdistraster"
backLink = "backlink2"
method = "EACH_CELL"
destField = "FID"

# Execute CostPath
outCostPath = CostPath(inDestination, costDistanceRaster, backLink, method,
                       destField)

# Save the output 
outCostPath.save("c:/sapyexamples/output/costpath02")