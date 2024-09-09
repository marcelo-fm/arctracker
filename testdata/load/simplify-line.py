# Name: SimplifyLine_Example2.py
# Description: Simplify line features from two feature classes, rivers and coastlines,
# while maintaining their connections

# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data/Portland.gdb/Hydrography"
 
# Set local variables
inRiverFeatures = "rivers"
inCoastlineFeatures = "coastlines"

mergedFeatures = "C:/data/PortlandOutput.gdb/merged_lines"
simplifiedFeatures = "C:/data/PortlandOutput.gdb/merged_lines_simplified"
tempLayer = "tempLyr"

outRiverFeatureClass = "C:/data/PortlandOutput.gdb/rivers_final"
outCoastlineFeatureClass = "C:/data/PortlandOutput.gdb/coastlines_final"

# Merge rivers and coastlines into one feature class, 
# assuming that they have a common f-code field 
# with value 40 for rivers and 80 for coastlines.
arcpy.management.Merge(inRiverFeatures, inCoastlineFeatures, mergedFeatures)

# Simplify all lines.
arcpy.cartography.SimplifyLine(mergedFeatures, 
                simplifiedFeatures, 
                "BEND_SIMPLIFY", 
                100, 
                "KEEP_COLLAPSED_POINTS")
 
# Select rivers and coastlines by their f-code values 
# and put them in separate feature classes.
arcpy.management.MakeFeatureLayer(simplifiedFeatures, tempLayer, "f-code = 40")
arcpy.management.CopyFeatures(tempLayer, outRiverFeatureClass)

arcpy.management.MakeFeatureLayer(simplifiedFeatures, tempLayer, "f-code = 80")
arcpy.management.CopyFeatures(tempLayer, outCoastlineFeatureClass)