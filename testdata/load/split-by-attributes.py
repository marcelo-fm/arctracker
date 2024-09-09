# Description: Use SplitByAttributes to split a feature class by unique values.

# Import required modules
import arcpy

# Set local variables
in_feature_class = 'c:/data/base.gdb/ecology'
target_workspace = 'c:/data/output.gdb'
fields = ['REGION', 'ECO_CODE']

arcpy.analysis.SplitByAttributes(in_feature_class, target_workspace, fields)