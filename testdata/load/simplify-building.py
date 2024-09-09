# Name: SimplifyBuilding_Example2.py
# Description: Aggregate building features and then simplify them.

# Import system modules
import arcpy
import arcpy.cartography as CA

# Set environment settings
arcpy.env.workspace = "C:/data/Portland.gdb/Buildings"

# Set local variables
inBuildingFeatures = "houses"
inBarrierFeatures = "roads"
aggregatedFeatures = "C:/data/PortlandOutput.gdb/residential_areas"
simplifiedFeatures = "C:/data/PortlandOutput.gdb/residential_simplified"

# Aggregate house polygons
CA.AggregatePolygons(inBuildingFeatures, aggregatedFeatures, 10, 100, 100, 
                     "ORTHOGONAL")

# Simplify residential building polygons
CA.SimplifyBuilding(aggregatedFeatures, simplifiedFeatures, 10, 100, 
                    "CHECK_CONFLICTS", inBarrierFeatures, 
                    "KEEP_COLLAPSED_POINTS")