# Name: DistanceAllocation_Ex_02.py
# Description: Calculates the distance allocation.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSources = "insources.shp"
inBarrier = "barriers.tif"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute EucDirections
outDistAlloc = DistanceAllocation(inSources, inBarrier)

# Save the output 
outDistAlloc.save("c:/sapyexamples/output/distAllo2.tif")