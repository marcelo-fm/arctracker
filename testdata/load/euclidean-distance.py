# Name: EucDistance_Ex_02.py
# Description: Calculates for each cell the Euclidean distance to the nearest source.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "rec_sites.shp"
maxDistance = 4000
cellSize = 4
outDirectionRaster = "C:/sapyexamples/output/eucdirect"

# Execute EucDistance
outEucDistance = EucDistance(inSourceData, maxDistance, cellSize, outDirectionRaster)

# Save the output 
outEucDistance.save("C:/sapyexamples/output/eucdist")