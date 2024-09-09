# Name: RegionGroup_Ex_02.py
# Description: Records, for each cell in the output, the
#              identity of the connected region to which 
#              it belongs within the Analysis window. A 
#              unique number is assigned to each region.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "land"
valToIgnore = 5

# Execute RegionGroup
outRegionGrp = RegionGroup(inRaster, "EIGHT", "CROSS", 
                           "NO_LINK", valToIgnore)

# Save the output 
outRegionGrp.save("C:/sapyexamples/output/reggrpout")