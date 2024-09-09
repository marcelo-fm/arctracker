'''****************************************************************************
Name: SurfaceContour Example
Description: This script demonstrates how to use the
             SurfaceContour tool.

****************************************************************************'''

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set Local Variables
inSurface = "sample.gdb/featuredataset/terrain"
outContour = arcpy.CreateUniqueName("contour.shp")

#Execute SurfaceContour
arcpy.ddd.SurfaceContour(inSurface, outContour, 10)