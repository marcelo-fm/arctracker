# Name: Test_Ex_02.py
# Description: Perform a Boolean evaluation of the input raster based
#              on a where clause
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"
inWhereClause = "VALUE > 100"

# Execute Test
outTest = Test(inRaster, inWhereClause)

# Save the output 
outTest.save("C:/sapyexamples/output/outtest")