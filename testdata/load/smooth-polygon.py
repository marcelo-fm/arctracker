# Name: SmoothPolygon_Example2.py
# Description: Eliminate small islands before simplifying and smoothing lake boundaries

# Import system modules
import arcpy
import arcpy.cartography as CA
import arcpy.management as DM

# Set environment settings
arcpy.env.workspace = "C:/data/Portland.gdb/Hydrography"

# Set local variables
inLakeFeatures = "lakes"
barriers = "C:/data/Portland.gdb/Structures/buildings"
eliminatedFeatures = "C:/data/PortlandOutput.gdb/lakes_eliminated"
simplifiedFeatures = "C:/data/PortlandOutput.gdb/lakes_simplified"
smoothedFeatures = "C:/data/PortlandOutput.gdb/lakes_smoothed"

# Eliminate small islands in lake polygons.
DM.EliminatePolygonPart(inLakeFeatures, eliminatedFeatures, 100, "OR", 0, 
                        "CONTAINED_ONLY")

# Simplify lake polygons.
CA.SimplifyPolygon(eliminatedFeatures, simplifiedFeatures, "POINT_REMOVE", 50, 
                   200, "RESOLVE_ERRORS", "KEEP_COLLAPSED_POINTS", barriers)

# Smooth lake polygons.
CA.SmoothPolygon(simplifiedFeatures, smoothedFeatures, "PAEK", 100, "", 
                 "FLAG_ERRORS", barriers)