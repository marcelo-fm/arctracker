# Name: PairwiseBuffer.py
# Description: Find areas of suitable vegetation that exclude areas heavily 
#              impacted by major roads.

# Import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/Habitat_Analysis.gdb"

# Select suitable vegetation patches from all vegetation
veg = "vegtype"
suitableVeg = "C:/output/Output.gdb/suitable_vegetation"
whereClause = "HABITAT = 1" 
arcpy.analysis.Select(veg, suitableVeg, whereClause)

# Buffer areas of impact around major roads
roads = "majorrds"
roadsBuffer = "C:/output/Output.gdb/buffer_output"
distanceField = "Distance"
dissolveType = "LIST"
dissolveField = "Distance"
arcpy.analysis.PairwiseBuffer(roads, roadsBuffer, distanceField, dissolveType, 
                              dissolveField)

# Erase areas of impact around major roads from the suitable vegetation patches
eraseOutput = "C:/output/Output.gdb/suitable_vegetation_minus_roads"
xyTol = "1 Meters"
arcpy.analysis.Erase(suitableVeg, roadsBuffer, eraseOutput, xyTol)