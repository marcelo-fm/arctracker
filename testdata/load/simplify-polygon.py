# Name: SimplifyPolygon_Example2.py
# Description: Eliminate small islands before simplifying and smoothing lake 
#              boundaries.

# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data/Portland.gdb/Hydrography"
 
# Set local variables
inLakeFeatures = "lakes"
eliminatedFeatures = "C:/data/PortlandOutput.gdb/lakes_eliminated"
simplifiedFeatures = "C:/data/PortlandOutput.gdb/lakes_simplified"
smoothedFeatures = "C:/data/PortlandOutput.gdb/lakes_smoothed"

# Eliminate small islands in lake polygons.
arcpy.management.EliminatePolygonPart(inLakeFeatures, eliminatedFeatures, 100, 
                                      "OR", 0, "CONTAINED_ONLY")
 
# Simplify lake polygons
arcpy.cartography.SimplifyPolygon(eliminatedFeatures, simplifiedFeatures, 
                                  "POINT_REMOVE", 50, 200, "#", 
                                  "KEEP_COLLAPSED_POINTS")

# Smooth lake polygons
arcpy.cartography.SmoothPolygon(simplifiedFeatures, smoothedFeatures, "PAEK", 100, 
                 "FLAG_ERRORS")