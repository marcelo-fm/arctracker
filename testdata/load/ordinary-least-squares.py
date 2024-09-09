# Analyze the growth of regional per capita incomes in US
# Counties from 1969 -- 2002 using Ordinary Least Squares Regression

# Import system modules
import arcpy

# Set property to overwrite existing outputs
arcpy.env.overwriteOutput = True

# Local variables...
workspace = r"C:\Data"

try:
    # Set the current workspace (to avoid having to specify the full path to the feature classes each time)
    arcpy.env.workspace = workspace

    # Growth as a function of {log of starting income, dummy for South
    # counties, interaction term for South counties, population density}
    # Process: Ordinary Least Squares... 
    ols = arcpy.stats.OrdinaryLeastSquares("USCounties.shp", "MYID", 
                        "olsResults.shp", "GROWTH",
                        "LOGPCR69;SOUTH;LPCR_SOUTH;PopDen69",
                        "olsCoefTab.dbf",
                        "olsDiagTab.dbf")

    # Create Spatial Weights Matrix (Can be based on input or output FC)
    # Process: Generate Spatial Weights Matrix... 
    swm = arcpy.stats.GenerateSpatialWeightsMatrix("USCounties.shp", "MYID",
                        "euclidean6Neighs.swm",
                        "K_NEAREST_NEIGHBORS",
                        "#", "#", "#", 6) 
                        
    # Calculate Moran's Index of Spatial Autocorrelation for 
    # OLS Residuals using a SWM File.  
    # Process: Spatial Autocorrelation (Morans I)...      
    moransI = arcpy.stats.SpatialAutocorrelation("olsResults.shp", "Residual",
                        "NO_REPORT", "GET_SPATIAL_WEIGHTS_FROM_FILE", 
                        "EUCLIDEAN_DISTANCE", "NONE", "#", 
                        "euclidean6Neighs.swm")

except:
    # If an error occurred when running the tool, print out the error message.
    print(arcpy.GetMessages())