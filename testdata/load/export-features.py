# Name: ExportFeatures_Example2.py
# Description: Use Export Features with an expression to create a subset of the
# original feature class.

# Import system modules

import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/SFValley.gdb"

# Set local variables
inFeatures = "streets"
outFeatureClass =  "C:/output/output.gdb/arterials"
expression = arcpy.AddFieldDelimiters(arcpy.env.workspace, "Category") + " = 'Arterials'"

# Run ExportFeatures
arcpy.conversion.ExportFeatures(inFeatures, outFeatureClass, expression,
                               "NOT_USE_ALIAS")