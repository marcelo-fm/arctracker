# Name: Shrink_Ex_02.py
# Description: Shrinks the selected zones by a 
#              specified number of cells.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "land"
cellRemove = 2
zoneSet = [1,3,7,9]

# Execute Shrink
outShrink = Shrink(inRaster, cellRemove, zoneSet)

# Save the output 
outShrink.save("c:/sapyexamples/output/outshrink")