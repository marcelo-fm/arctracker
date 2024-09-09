# Cluster sampling

# Create 100 cluster polygons that are diamond shaped.

# Import system modules.
import arcpy

# Allow overwriting output.
arcpy.env.overwriteOutput = True

# Define the study area and output features.
inputStudyArea = "C:/samplingdata/inputs.gdb/study_area_polygons"
outputFeatures = "C:/samplingdata/outputs.gdb/out_samples_CLUST"

# Define the sampling method.
samplingMethod = "CLUSTER"

# Create a diamond tessellation and randomly choose 100 polygons.
binShape = "DIAMOND"
binSize = "1000000 SquareFeet"
numSamples=100
spatialRelationship = "INTERSECT"

# Run tool.
try:
    arcpy.management.CreateSpatialSamplingLocations(inputStudyArea, outputFeatures,
                     samplingMethod, "", "", binShape, binSize, "", numSamples, "",
                     "", "", "", spatialRelationship)

except arcpy.ExecuteError:
    # If an error occurred when running the tool, print the error message.
    print(arcpy.GetMessages())