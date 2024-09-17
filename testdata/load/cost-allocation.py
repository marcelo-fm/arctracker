# Name: CostAllocation_Ex_02.py
# Description: Calculates for each cell its nearest source 
#              based on the least accumulative cost over a 
#              cost surface.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inFeature = "observers.shp"
costRaster = "costraster"
maxDist = 25000
valRaster = "elevation"
featField = "FID"
outDistanceRaster = "c:/sapyexamples/output/distout"
outBacklink = "c:/sapyexamples/output/backlinkout"

# Execute CostAllocation
costAllocOut = CostAllocation(inFeature, costRaster, maxDist,
                              valRaster, featField, outDistanceRaster,
                              outBacklink)

# Save the output 
costAllocOut.save("c:/sapyexamples/output/costalloc01")