# Name: Con_Ex_02.py
# Description: Performs a conditional if/else evaluation 
#              on each cell of an input raster.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = Raster("elevation")
inTrueRaster = 1
inFalseConstant = 0
whereClause = "VALUE >= 1500"

# Execute Con
outCon = Con(inRaster, inTrueRaster, inFalseConstant, whereClause)

# Execute Con using a map algebra expression instead of a where clause
outCon2 = Con(inRaster >= 1500, inTrueRaster, inFalseConstant)

# Save the outputs 
outCon.save("C:/sapyexamples/output/outcon")
outCon2.save("C:/sapyexamples/output/outcon2")