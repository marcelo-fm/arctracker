# Description: Run Integrate on a feature class
 
# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data/Habitat_Analysis.gdb"
 
# Set local variables
inFeatures = "vegtype"
integrateFeatures = "C:/output/output.gdb/vegtype"
 
# Run CopyFeatures (since Integrate modifies the original data,
#  this ensures the original is preserved)
arcpy.management.CopyFeatures(inFeatures, integrateFeatures)
 
# Run Integrate
arcpy.management.Integrate(integrateFeatures)