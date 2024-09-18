# Name: EucDirection_Ex_02.py
# Description: Calculates the direction in degrees that each 
#              cell center is from the cell center of the 
#              closest source.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSource = "observers.shp"
maxDist = 35000
cellSize = 50
optOutDistance = "c:/sapyexamples/output/optdistout"

# Execute EucDirections
outEucDirect = EucDirection(inSource, maxDist, cellSize, 
                            optOutDistance)

# Save the output 
outEucDirect.save("c:/sapyexamples/output/eucoutdir02")