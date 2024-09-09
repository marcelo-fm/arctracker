# Name: Eliminate_Example2.py
# Description: Eliminate features based on a selection.
 
# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data/Portland.gdb/Census"
 
# Set local variables
inFeatures = "blockgrp"
tempLayer = "blocklayer"
expression = '"Area_Sq_Miles" < 0.15'
outFeatureClass = "C:/output/output.gdb/eliminate_output"
exclusionExpression = '"OBJECTID" = 9'
 
# Execute MakeFeatureLayer
arcpy.MakeFeatureLayer_management(inFeatures, tempLayer)
 
# Execute SelectLayerByAttribute to define features to be eliminated
arcpy.SelectLayerByAttribute_management(tempLayer, "NEW_SELECTION", expression)
 
# Execute Eliminate
arcpy.Eliminate_management(tempLayer, outFeatureClass, "LENGTH", 
                           exclusionExpression)