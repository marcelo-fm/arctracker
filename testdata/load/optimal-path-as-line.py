# Name: OptimalPathAsLine_Ex_02.py
# Description: Calculates the least-cost path from a source to 
#              a destination.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inDestination = "observers.shp"
inDistAccum = "accumraster.tif"
inBackDir = "backdir2.tif"
outPathFeat = "c:/sapyexamples/output.gdb/optimalfeaturepaths02"
destField = "FID"
method = "EACH_CELL"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute
OptimalPathAsLine(inDestination, inDistAccum, inBackDir, 
                  outPathFeat, destField, method)