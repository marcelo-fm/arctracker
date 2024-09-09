# Name: ExtractByPoints_Ex_02.py
# Description: Extracts the cells of a raster based on a set of points.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "soil"
pointList = [arcpy.Point(743050, 4321275), 
             arcpy.Point(743100, 4321200), 
             arcpy.Point(743500, 4322000),
             arcpy.Point(742900, 4321800)]

# Execute ExtractByPoints
outPointExtract = ExtractByPoints("soil", pointList,"INSIDE")

# Save the output 
outPointExtract.save("c:/sapyexamples/output/pntext")