# Name: LineDensity_Ex_02.py
# Description: Calculates a magnitude per unit area from polyline features
#    that fall within a radius around each cell.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPolylineFeatures = "roads.shp"
populationField = "length"
cellSize = 120
searchRadius = 1500

# Execute LineDensity
outLineDensity = LineDensity(inPolylineFeatures, populationField, cellSize,
                             searchRadius, "SQUARE_MILES") 

# Save the output 
outLineDensity.save("C:/sapyexamples/output/linedensity")