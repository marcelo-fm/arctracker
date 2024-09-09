# Description: Run PairwiseIntegrate on a feature class

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/Habitat_Analysis.gdb"

# Set local variables
inFeatures = "vegtype"
integrateFeatures = "C:/output/output.gdb/vegtype"

# Run CopyFeatures (since PairwiseIntegrate modifies the original data, this 
# ensures the original is preserved)
arcpy.management.CopyFeatures(inFeatures, integrateFeatures)

# Run PairwiseIntegrate
arcpy.analysis.PairwiseIntegrate(integrateFeatures)