# Name: InList_Ex_02.py
# Description: Determines which values from the first input are
#              contained in the other inputs
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = "redlandsc1"
inRaster2 = "redlandsc2"
inRaster3 = "redlandsc3"

# Execute InList
outInList = InList(inRaster1, [inRaster2, inRaster3])

# Save the output 
outInList.save("C:/sapyexamples/output/outinlist")