# Name: LineStatistics_Ex_02.py
# Description: 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inLines = "streams.shp"
field = "LENGTH"
cellSize = 50
searchRadius = 500

# Execute LineStatistics
lineStatOut = LineStatistics(inLines, field, cellSize, searchRadius,
                              "MEAN")

# Save the output 
lineStatOut.save("C:/sapyexamples/output/linestatisout")