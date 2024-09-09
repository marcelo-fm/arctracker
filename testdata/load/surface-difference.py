'''****************************************************************************
Name: SurfaceDifference Example
Description: This script demonstrates how to use the
             SurfaceDifference tool.
****************************************************************************'''

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set Local Variables
inSurface = "flood_tin"
inReference = "elev_tin"

# Ensure output name is unique
outPoly = arcpy.CreateUniqueName("difference.shp")

# Execute SurfaceDifference
arcpy.ddd.SurfaceDifference(inSurface, inReference, outPoly)