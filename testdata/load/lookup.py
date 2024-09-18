# Name: lookup_example02.py
# Description: Creates a new raster by looking up values found in another 
#              field in the table of the input raster.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "mycity"
lookupField = "land_code"

# Execute Lookup
outRaster = Lookup(inRaster, lookupField)

# Save the output 
outRaster.save("C:/sapyexamples/output/mylandcode")