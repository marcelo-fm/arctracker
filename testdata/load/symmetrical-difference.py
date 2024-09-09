# Name: SymDiff_Example2.py
# Description: Create symmetrical difference between input and update features
 
# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data"
 
# Set local variables
inFeatures = "climate.shp"
updateFeatures = "elevlt250.shp"
outFeatureClass = "C:/output/symdiff.shp"
clusterTolerance = 0.001
 
# Run SymDiff
arcpy.analysis.SymDiff(inFeatures, updateFeatures, outFeatureClass, "ALL",
                       clusterTolerance)