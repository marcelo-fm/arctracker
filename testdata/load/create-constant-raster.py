# Name: CreateConstantRaster_Ex_02.py
# Description: Creates a raster from a constant value
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy.sa import *

# Set local variables
constantValue = 12
cellSize = 2
outExtent = Extent(0, 0, 250, 250)

# Execute CreateConstantRaster
outConstRaster = CreateConstantRaster(constantValue, "FLOAT", cellSize,
                                      outExtent)

# Save the output 
outConstRaster.save("C:/sapyexamples/output/outconst")