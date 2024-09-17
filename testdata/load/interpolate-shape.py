# Name: InterpolateShape_Ex_02.py
# Description: This script demonstrates how to use InterpolateShape on the 2D
# features in a target workspace.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
inFeatureClass = "point.shp"
inSurface = "dtm_tin"
OutFeatureClass = "point_interp.shp"
method = "NEAREST"

# Execute the tool
InterpolateShape(inSurface, inFeatureClass, OutFeatureClass, 15, 1, method, True)