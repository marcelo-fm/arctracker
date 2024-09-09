# Name: EliminatePolygonPart_Example2.py
# Description: Eliminate small islands before simplifying and smoothing lake boundaries
 
# Import system modules
import arcpy
from arcpy import env
 
# Set environment settings
env.workspace = "C:/data/Portland.gdb/Hydrography"
 
# Set local variables
inLakeFeatures = "lakes"
eliminatedFeatures = "lakes_eliminated"
simplifiedFeatures = "lakes_simplified"
smoothedFeatures = "lakes_smoothed"

# Eliminate small islands in lake polygons.
arcpy.EliminatePolygonPart_management(inLakeFeatures, eliminatedFeatures, "AREA", 100, "", "CONTAINED_ONLY")
 
# Simplify lake polygons.
arcpy.SimplifyPolygon_cartography(eliminatedFeatures, simplifiedFeatures, "POINT_REMOVE", 50, 200, "RESOLVE_ERRORS", "KEEP_COLLAPSED_POINTS")
 
# Smooth lake polygons.
arcpy.SmoothPolygon_cartography(simplifiedFeatures, smoothedFeatures, "BEZIER_INTERPOLATION")