# Name: OptimalRegionConnections_Ex_02.py
# Description: Calculates the optimal network of connections for the sources.
#
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "sources.shp"
inBarrier = "barriers.tif"
inCostRaster = "cost_surface.tif"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute the tool
outOptRegConnect = OptimalRegionConnections(inSourceData, inBarrier, inCostRaster)

# Save the output 
outOptRegConnect.save("C:/sapyexamples/output/optregconnect.tif")