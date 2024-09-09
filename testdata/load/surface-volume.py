'''****************************************************************************
Name: Surface Volume Example
Description: This script demonstrates how to use the
             Surface Volume tool.

****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set Local Variables
inSurface = "elevation_tin"

# Execute SurfaceVolume
result = arcpy.ddd.SurfaceVolume(inSurface, "", "ABOVE", "300", "1", "5")
print(result.getMessages())