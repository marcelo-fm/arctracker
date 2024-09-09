# Analyze the spatial distribution of 911 calls in a metropolitan area
# using the Hot-Spot Analysis Tool (Local Gi*)

# Import system modules
import arcpy

# Set property to overwrite existing output, by default
arcpy.env.overwriteOutput = True

# Local variables...
workspace = "C:/Data"

try:
    # Set the current workspace (to avoid having to specify the full path to the feature classes each time)
    arcpy.env.workspace = workspace

    # Copy the input feature class and integrate the points to snap
    # together at 500 feet
    # Process: Copy Features and Integrate
    cf = arcpy.CopyFeatures_management("911Calls.shp", "911Copied.shp",
                         "#", 0, 0, 0)

    integrate = arcpy.Integrate_management("911Copied.shp #", "500 Feet")

    # Use Collect Events to count the number of calls at each location
    # Process: Collect Events
    ce = arcpy.CollectEvents_stats("911Copied.shp", "911Count.shp", "Count", "#")

    # Add a unique ID field to the count feature class
    # Process: Add Field and Calculate Field
    af = arcpy.AddField_management("911Count.shp", "MyID", "LONG", "#", "#", "#", "#",
                     "NON_NULLABLE", "NON_REQUIRED", "#",
                     "911Count.shp")
    
    cf = arcpy.CalculateField_management("911Count.shp", "MyID", "[FID]", "VB")

    # Create Spatial Weights Matrix for Calculations
    # Process: Generate Spatial Weights Matrix... 
    swm = arcpy.GenerateSpatialWeightsMatrix_stats("911Count.shp", "MYID",
                        "euclidean6Neighs.swm",
                        "K_NEAREST_NEIGHBORS",
                        "#", "#", "#", 6,
                        "NO_STANDARDIZATION") 

    # Hot Spot Analysis of 911 Calls
    # Process: Hot Spot Analysis (Getis-Ord Gi*)
    hs = arcpy.HotSpots_stats("911Count.shp", "ICOUNT", "911HotSpots.shp", 
                     "GET_SPATIAL_WEIGHTS_FROM_FILE",
                     "EUCLIDEAN_DISTANCE", "NONE",
                     "#", "#", "euclidean6Neighs.swm")

except arcpy.ExecuteError:
    # If an error occurred when running the tool, print the error message
    print(arcpy.GetMessages())