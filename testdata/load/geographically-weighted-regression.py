# Model 911 emergency calls using GWR

# Import system modules
import arcpy

# Set property to overwrite existing outputs
arcpy.env.overwriteOutput = True

# Local variables...
workspace = r"C:\Data"

try:
    # Set the current workspace (to avoid having to specify the full path to the 
    # feature classes each time)
    arcpy.env.workspace = workspace

    # 911 Calls as a function of {number of businesses, number of rental units,
    # number of adults who didn't finish high school}
    # Process: Geographically Weighted Regression... 
    gwr = arcpy.stats.GeographicallyWeightedRegression("CallData.shp", "Calls", 
                        "BUS_COUNT;RENTROCC00;NoHSDip",
                        "CallsGWR.shp", "ADAPTIVE", "BANDWIDTH PARAMETER", "#", "25", "#",
                        "CoefRasters", "135", "PredictionPoints", "#", "GWRCallPredictions.shp")

    # Create Spatial Weights Matrix to use with Global Moran's I tool
    # Process: Generate Spatial Weights Matrix... 
    swm = arcpy.stats.GenerateSpatialWeightsMatrix("CallsGWR.shp", "UniqID",
                        "CallData25Neighs.swm",
                        "K_NEAREST_NEIGHBORS",
                        "#", "#", "#", 25) 
                        
    # Calculate Moran's Index of Spatial Autocorrelation for 
    # OLS Residuals using a SWM File.  
    # Process: Spatial Autocorrelation (Morans I)...      
    moransI = arcpy.stats.SpatialAutocorrelation("CallsGWR.shp", "StdResid",
                        "NO_REPORT", "GET_SPATIAL_WEIGHTS_FROM_FILE", 
                        "EUCLIDEAN_DISTANCE", "NONE", "#", 
                        "CallData25Neighs.swm")

except arcpy.ExecuteError:
    # If an error occurred when running the tool, print out the error message.
    print(arcpy.GetMessages())