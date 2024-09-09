# Name: ExtractByPolgyon_Ex_02.py
# Description: Extracts the cells of a raster based on a polygon.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "soil"
polyPoints = [arcpy.Point(743050, 4321275), arcpy.Point(743100, 4321200), 
             arcpy.Point(743500, 4322000),arcpy.Point(742900, 4321800)]

# Execute ExtractByPolygon
extPolygonOut = ExtractByPolygon(inRaster, polyPoints, "INSIDE")

# Save the output 
extPolygonOut.save("c:/sapyexamples/output/extpoly02")