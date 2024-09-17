# Create a Spatial Weights Matrix based on Network Data 

# Import system modules
import arcpy

# Set the environment property to overwrite existing output
arcpy.env.overwriteOutput = True

# Check out the ArcGIS Network Analyst extension (required for the Generate Network Spatial Weights tool)
arcpy.CheckOutExtension("Network")

# Local variables...
workspace = r"C:\Data"

try:
    # Set the current workspace (to avoid having to specify the full path to 
    # the feature classes each time)
    arcpy.env.workspace = workspace

    # Create Spatial Weights Matrix based on Network Data 
    # Process: Generate Network Spatial Weights... 
    nwm = arcpy.stats.GenerateNetworkSpatialWeights("Hospital.shp", "MyID",
                        "network6Neighs.swm", "Streets_ND",
                        "MINUTES", 10, 6, "#", "ALLOW_UTURNS",
                        "#", "USE_HIERARCHY", "#", "INVERSE",
                        1, "ROW_STANDARDIZATION")

    # Create Spatial Weights Matrix based on Euclidean Distance
    # Process: Generate Spatial Weights Matrix... 
    swm = arcpy.stats.GenerateSpatialWeightsMatrix("Hospital.shp", "MYID",
                        "euclidean6Neighs.swm",
                        "K_NEAREST_NEIGHBORS",
                        "#", "#", "#", 6) 

    # Calculate Moran's Index of Spatial Autocorrelation for 
    # average hospital visit times using Network Spatial Weights 
    # Process: Spatial Autocorrelation (Morans I)...       
    moransINet = arcpy.stats.SpatialAutocorrelation("Hospital.shp", "VisitTime",
                        "NO_REPORT", "GET_SPATIAL_WEIGHTS_FROM_FILE", 
                        "EUCLIDEAN_DISTANCE", "NONE", "#", 
                        "network6Neighs.swm")

    # Calculate Moran's Index of Spatial Autocorrelation for 
    # average hospital visit times using Euclidean Spatial Weights   
    # Process: Spatial Autocorrelation (Morans I)...       
    moransIEuc = arcpy.stats.SpatialAutocorrelation("Hospital.shp", "VisitTime",
                        "NO_REPORT", "GET_SPATIAL_WEIGHTS_FROM_FILE", 
                        "EUCLIDEAN_DISTANCE", "NONE", "#", 
                        "euclidean6Neighs.swm")

except:
    # If an error occurred when running the tool, print out the error message.
    print arcpy.GetMessages()