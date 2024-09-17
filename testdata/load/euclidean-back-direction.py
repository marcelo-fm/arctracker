# Name: EucBackDirection_Ex_02.py
# Description: Calculates, for each cell, the direction,
#              in degrees, to the neighboring cell along
#              the shortest path back to the closest
#              source while avoiding barriers.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSource = "observers.shp"
inBarriers = "rivers.tif"
maxDist = 35000
cellSize = 50
distMethod = "GEODESIC"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute EucDirections
outEucBackDir = EucBackDirection(inSource, inBarriers, maxDist,
                            cellSize, distMethod)

# Save the output 
outEucBackDir.save("c:/sapyexamples/output/eucoutbackdir02.tif")