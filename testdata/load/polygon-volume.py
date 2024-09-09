'''****************************************************************************
Name: PolygonVolume Example
Description: This script demonstrates how to use the 
             PolygonVolume tool.
****************************************************************************'''

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"


# Set Local Variables
inSurface = "sample.gdb/featuredataset/terrain"
inPoly = "floodplain_100.shp"
zField = "Height"
refPlane = "BELOW"
volFld = "Volume"
sAreaFld = "SArea"

#Execute PolygonVolume
arcpy.ddd.PolygonVolume(inSurface, inPoly, zField, refPlane, volFld, sAreaFld)