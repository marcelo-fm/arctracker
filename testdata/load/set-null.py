# Name: SetNull_Ex_02.py
# Description: Returns NoData if a conditional evaluation is 
#              true and returns the value specified by another
#              raster if it is false, on a cell-by-cell basis.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "landclass"
inFalseRaster = 1
whereClause = "VALUE <> 7"

# Execute SetNull
outSetNull = SetNull(inRaster, inFalseRaster, whereClause)

# Save the output 
outSetNull.save("C:/sapyexamples/output/outsetnull")