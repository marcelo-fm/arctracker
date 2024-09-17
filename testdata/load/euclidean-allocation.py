# Name: EucAllocation_Ex_02.py
# Description: Calculates, for each cell, the zone of the closest 
#              source location in Euclidean distance.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSource = "observers.shp"
maxDist = 50000
valRaster = "elevation"
cellSize = 25
sourceField = "FID"
optOutDist = "c:/sapyexamples/output/outeucdist02"
optOutDir = "c:/sapyexamples/output/outeucdir02"

# Execute EucAllocation
eucAllocate = EucAllocation(inSource, maxDist, valRaster, cellSize,
                             sourceField, optOutDist, optOutDir)

# Save the output 
eucAllocate.save("c:/sapyexamples/output/eucalloc02")