# Name: OptimalCorridorConnections_standalone.py
# Description: Calculates corridor.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set environment settings
env.workspace = "C:/arcpyexamples/data"

# Set local variables
regions = "Lakes.tif"
outCorridors = "NewCorridors.shp"
roadBarriers = "Roads.shp"
costSurface = "CostSurface.tif"
optimalLines = "OutCorridorCenterLines.shp"
outAllCorridors = "OutAllCorridors.shp"
outAllLines = "OutAllCenterLines.shp"
corridorMethod = "FIXED_WIDTH_CORRIDOR"
corridorWidth = 5000
distanceMethod = "GEODESIC"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute  OptimalCorridorConnections

OptimalCorridorConnections(regions, outCorridors, roadBarriers,
                           costSurface, optimalLines,
                           outAllCorridors, outAllLines,
                           corridorMethod, corridorWidth, distanceMethod)