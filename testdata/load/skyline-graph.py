'''****************************************************************************
Name: Skyline Example
Description: This script demonstrates how to use the 
             Skyline tool.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data'

# Set Local Variables
inPts = "observers.shp"
inLines = "skyline_outline.shp"
baseVisibility = 25

# Ensure output table has unique name
outTable = arcpy.CreateUniqueName("angles_table.dbf")

#Execute SkylineGraph
arcpy.ddd.SkylineGraph(inPts, inLines, 0, "ADDITIONAL_FIELDS", outTable)