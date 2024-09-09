'''****************************************************************************
Name: InterpolatePolyToPatch Example
Description: This script demonstrates how to use the
             InterpolatePolyToPatch tool.
****************************************************************************'''

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set Local Variables
inTerrain = "sample.gdb/featuredataset/terrain"
inPoly = "polygon.shp"
outMP = arcpy.CreateUniqueName("out_multipatch.shp")

#Execute InterpolatePolyToPatch
arcpy.ddd.InterpolatePolyToPatch(inTerrain, inPoly, outMP, 1024, 1, "Area", "SArea", 5)