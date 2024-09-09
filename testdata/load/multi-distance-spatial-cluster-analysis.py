# Use Ripley's K-Function to analyze the spatial distribution of 911
# calls in Portland Oregon 

# Import system modules
import arcpy

# Set property to overwrite existing outputs
arcpy.env.overwriteOutput = True

# Local variables...
workspace = r"C:\Data"

try:
    # Set the current workspace (to avoid having to specify the full 
    # path to the feature classes each time)
    arcpy.env.workspace = workspace

    # Set Distance Band Parameters: Analyze clustering of 911 calls from
    # 1000 to 3000 feet by 200 foot increments
    numDistances = 11
    startDistance = 1000.0
    increment = 200.0

    # Process: Run K-Function...
    kFun = arcpy.stats.MultiDistanceSpatialClustering("911Calls.shp",
                        "kFunResult.dbf", numDistances,
                        "0_PERMUTATIONS_-_NO_CONFIDENCE_ENVELOPE", 
                        "NO_DISPLAY", "#", startDistance, increment,
                        "REDUCE_ANALYSIS_AREA",
                        "MINIMUM_ENCLOSING_RECTANGLE", "#")

except:
    # If an error occurred when running the tool, print out the error message.
    print(arcpy.GetMessages())