# Name: calculateadjacentfields_example.py
# Description: Create and populate fields identifying adjacent features for a
# regular polygon grid feature class
# Author: ESRI

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
arcpy.env.workspace = "C:\Data\ProjectData.gdb"

# Set local variables
inFeatures = "MyPolygonIndex"
inField = "PageName"

# Execute CalculateAdjacentFields
arcpy.CalculateAdjacentFields_cartography (inFeatures, inField)