# Name: AddSurfaceInformation_Ex_02.py
# Description: This script demonstrates how to use AddSurfaceInformation 
# on a 2D point feature class in a target workspace.
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
Prop = "Z"
method = "LINEAR"
pyramid = 5

# Execute the tool
AddSurfaceInformation(inFeatureClass, inSurface, Prop, method, 15, 1, pyramid)