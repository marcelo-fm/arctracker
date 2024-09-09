# Name: CreateNormalRaster_Ex_02.py
# Description: Creates a raster of random values from a normal distribution
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
cellSize = 2
extent = Extent(0, 0, 150, 150)

# Execute CreateNormalRaster
outNormalRaster = CreateNormalRaster(cellSize, extent) 

# Save the output 
outNormalRaster.save("C:/sapyexamples/output/outnormraster")