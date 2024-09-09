# Name: ExtractByAttributes_Ex_02.py
# Description: Extracts the cells of a raster based on a logical query. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
inSQLClause = "VALUE > 1000"

# Execute ExtractByAttributes
attExtract = ExtractByAttributes(inRaster, inSQLClause) 

# Save the output 
attExtract.save("c:/sapyexamples/output/attextract02")