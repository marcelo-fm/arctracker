# Create a Spatial Weights Matrix based on Network Data

# Import system modules
import arcpy

# Set the environment property to overwrite existing output
arcpy.env.overwriteOutput = True

# Check out the ArcGIS Network Analyst extension 
arcpy.CheckOutExtension("Network")

# Local variables...
workspace = r"c:\Data"

try:
    # Set the current workspace (to avoid having to specify the full path to
    # the feature classes each time)
    arcpy.env.workspace = workspace

    # Create Spatial Weights Matrix based on Network Data
    # Process: Generate Network Spatial Weights...
    arcpy.stats.GenerateNetworkSWM(r"Data.gdb\Hospital","MyID", 
        "Hospital.swm", r"Data.gdb\Transportation\Streets_ND",
        "Driving Time", None, None, None, None, None, 
        "LOCAL_TIME_AT_LOCATIONS", None, "5000 Meters", "FIXED", 
        1,"ROW_STANDARDIZATION")

    # Create Spatial Weights Matrix based on Euclidean Distance
    # Process: Generate Spatial Weights Matrix...

    arcpy.stats.GenerateSpatialWeightsMatrix(
        r"Data.gdb\Hospital", "MyID", r"Euclidean6Neighs.swm", 
        "K_NEAREST_NEIGHBORS", "EUCLIDEAN", 1, None, 6, 
        "ROW_STANDARDIZATION", None, None, '', None, None)


    # Calculate Moran's Index of Spatial Autocorrelation for
    # average hospital visit times using Network Spatial Weights
    # Process: Spatial Autocorrelation (Morans I)...

    moransINet = arcpy.stats.SpatialAutocorrelation("Data.gdb\Hospital", 
                     "VisitTime", "NO_REPORT", "GET_SPATIAL_WEIGHTS_FROM_FILE",
                     "EUCLIDEAN_DISTANCE", "ROW", None, "Hospital.swm", None)

    # Calculate Moran's Index of Spatial Autocorrelation for
    # average hospital visit times using Euclidean Spatial Weights
    # Process: Spatial Autocorrelation (Morans I)...
    moransIEuc = arcpy.stats.SpatialAutocorrelation("Data.gdb\Hospital", 
                     "VisitTime", "NO_REPORT", "GET_SPATIAL_WEIGHTS_FROM_FILE",
                     "EUCLIDEAN_DISTANCE", "ROW", None, r"Euclidean6Neighs.swm", 
                     None)

except arcpy.ExecuteError:
    # If an error occurred when running the tool, print out the error message.
    print(arcpy.GetMessages())