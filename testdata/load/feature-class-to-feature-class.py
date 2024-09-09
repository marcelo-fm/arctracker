# Name: FeatureClassToFeatureClass_Example2.py
# Description: Use FeatureClassToFeatureClass with an expression to create a subset
#  of the original feature class.  
 
# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data/GreenvalleyDB.gdb/Public Buildings"
 
# Set local variables
inFeatures = "buildings_point"
outLocation = "C:/output/output.gdb"
outFeatureClass = "postoffices"
delimitedField = arcpy.AddFieldDelimiters(arcpy.env.workspace, "NAME")
expression = delimitedField + " = 'Post Office'"
 
# Run FeatureClassToFeatureClass
arcpy.conversion.FeatureClassToFeatureClass(inFeatures, outLocation, 
                                            outFeatureClass, expression)