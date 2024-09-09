# Analyze the spatial distribution of 911 calls in a metropolitan area
# using the Cluster-Outlier Analysis Tool (Anselin's Local Moran's I)

# Import system modules
import arcpy

# Set property to overwrite outputs if they already exist
arcpy.env.overwriteOutput = True

# Local variables...
workspace = r"C:\Data\911Calls"

try:
    # Set the current workspace 
    #  (to avoid having to specify the full path to the feature classes each time)
    arcpy.env.workspace = workspace

    # Copy the input feature class and integrate the points to snap
    # together at 500 feet
    # Process: Copy Features and Integrate
    cf = arcpy.CopyFeatures_management("911Calls.shp", "911Copied.shp")

    integrate = arcpy.Integrate_management("911Copied.shp #", "500 Feet")

    # Use Collect Events to count the number of calls at each location
    # Process: Collect Events
    ce = arcpy.CollectEvents_stats("911Copied.shp", "911Count.shp", "Count", "#")

    # Add a unique ID field to the count feature class
    # Process: Add Field and Calculate Field
    af = arcpy.AddField_management("911Count.shp", "MyID", "LONG", "#", "#", "#", "#",
                     														"NON_NULLABLE", "NON_REQUIRED", "#",
                     														"911Count.shp")
    
    cf = arcpy.CalculateField_management("911Count.shp", "MyID", "!FID!", "PYTHON")

    # Create Spatial Weights Matrix for Calculations
    # Process: Generate Spatial Weights Matrix... 
    swm = arcpy.GenerateSpatialWeightsMatrix_stats("911Count.shp", "MYID",
                        																											"euclidean6Neighs.swm",
                       																											 "K_NEAREST_NEIGHBORS",
                       															 												"#", "#", "#", 6) 

    # Cluster/Outlier Analysis of 911 Calls
    # Process: Local Moran's I
    clusters = arcpy.ClustersOutliers_stats("911Count.shp", "ICOUNT", 
                      																				  "911ClusterOutlier.shp", 
                        																				"GET_SPATIAL_WEIGHTS_FROM_FILE",
                        																				"EUCLIDEAN_DISTANCE", "NONE",
                       							 													"#", "euclidean6Neighs.swm", "NO_FDR", "499")

except arcpy.ExecuteError:
    # If an error occurred when running the tool, print out the error message.
    print(arcpy.GetMessages())