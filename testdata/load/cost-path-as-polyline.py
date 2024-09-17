# Name: CostPathAsPolyline_Ex_02.py
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
inCostDistRaster = "costdistraster"
inBacklink = "backlink2"
outCostPathFeat = "c:/sapyexamples/output.gdb/outcostpathfeat02"
method = "EACH_CELL"
destField = "FID"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute
CostPathAsPolyline(inDestination, inCostDistRaster, inBacklink, 
                   outCostPathFeat, method, destField)