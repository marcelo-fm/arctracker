# Name: Square_Ex_02.py
# Description: Calculates the square of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute Square
outSquare = Square(inRaster)

# Save the output 
outSquare.save("C:/sapyexamples/output/outsquare")