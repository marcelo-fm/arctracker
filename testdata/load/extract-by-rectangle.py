# Name: ExtractByRectangle_Ex_02.py
# Description: 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
inRectangle = Extent(477625, 213900, 486400, 224200)

# Execute ExtractByRectangle
rectExtract = ExtractByRectangle(inRaster, inRectangle, "INSIDE")

# Save the output 
rectExtract.save("c:/sapyexamples/output/extrect02")