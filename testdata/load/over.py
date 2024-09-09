# Name: Over_Ex_02.py
# Description: Returns those values from the first input that are
#    non-zero; otherwise, returns the value from the second input
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = "degs"
inRaster2 = "negs"

# Execute Over
outOver = Over(inRaster1, inRaster2)

# Save the output 
outOver.save("C:/sapyexamples/output/outover")