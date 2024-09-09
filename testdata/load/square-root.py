# Name: SquareRoot_Ex_02.py
# Description: Calculates the square root of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"

# Execute SquareRoot
outSQRT = SquareRoot(inRaster)

# Save the output 
outSQRT.save("C:/sapyexamples/output/outsqrt")