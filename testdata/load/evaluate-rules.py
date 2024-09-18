# Import arcpy
import arcpy

# Assign local variables
in_workspace = "https://myserver/server/rest/services/myservicename/FeatureServer"
extent = "-113.187897827702 38.0958054854392 -113.142166008849 38.1404599940719"

# Run the evaluation
arcpy.management.EvaluateRules(in_workspace, "VALIDATION_RULES", extent, "ASYNC")