# Name: CostDistance_Ex_02.py
# Description: Calculates for each cell the least accumulative cost distance
#    to the nearest source over a cost  surface. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "elevation"
maxDistance = 20000000   
outBkLinkRaster = "C:/sapyexamples/output/outbklink"

# Execute CostDistance
outCostDistance = CostDistance(inSourceData, inCostRaster, maxDistance, outBkLinkRaster)

# Save the output 
outCostDistance.save("C:/sapyexamples/output/outcostdist")