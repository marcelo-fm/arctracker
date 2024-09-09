'''****************************************************************************
Name: ExtrudeBetween Example
Description: This script demonstrates how to use the
             ExtrudeBetween tool.
****************************************************************************'''

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set Local Variables
inTIN1 = "ceiling"
inTIN2 = "floor"
inPoly = "study_area.shp"

# Ensure output has a unique name
outMP = arcpy.CreateUniqueName("extrusion.shp")

#Execute ExtrudeBetween
arcpy.ddd.ExtrudeBetween(inTIN1, inTIN2, inPoly, outMP)