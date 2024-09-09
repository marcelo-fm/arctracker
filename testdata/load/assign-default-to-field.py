# Name: AssignDefaultToField_Example2.py
# Description: Assign a new default to a field along with subtypes
 
# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "c:/data/Montgomery.gdb/Landbase"
 
# Set local variables
inFeatures = "blocks"
outFeatureClass = "c:/output/output.gdb/blocks"
fieldName = "Res"
defaultValue = 1
subTypes = ["0: Non-Residental", "1: Residental"]
 
# Execute CopyFeatures to make new copy of the input
arcpy.CopyFeatures_management(inFeatures, outFeatureClass)
 
# Execute AssignDefaultToField
arcpy.AssignDefaultToField_management(outFeatureClass, fieldName, 
                                      defaultValue, subTypes)