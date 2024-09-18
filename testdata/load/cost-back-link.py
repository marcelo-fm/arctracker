# Name: CostBackLink_Ex_02.py
# Description: Defines the neighbor that is the next cell on 
#              the least accumulative cost path to the nearest 
#              source.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSource = "observers.shp"
inCostRaster = "costraster"
inMaxDist = 100000
outDistRast = "c:/sapyexamples/output/distRast"

# Execute CostBackLink
outBacklink = CostBackLink(inSource,inCostRaster, inMaxDist,
                           outDistRast)

# Save the output 
outBacklink.save("c:/sapyexamples/output/backlink.tif")