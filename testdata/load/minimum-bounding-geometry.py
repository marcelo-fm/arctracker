# Name: MinimumBoundingGeometry.py
# Description: Use MinimumBoundingGeometry function to find an area 
#              for each multipoint input feature.

# import system modules 
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Create variables for the input and output feature classes
inFeatures = "treeclusters.shp"
outFeatureClass = "forests.shp"

# Use MinimumBoundingGeometry function to get a convex hull area
#         for each cluster of trees which are multipoint features
arcpy.MinimumBoundingGeometry_management(inFeatures, outFeatureClass, 
                                         "CONVEX_HULL", "NONE")