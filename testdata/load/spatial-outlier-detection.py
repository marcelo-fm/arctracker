# Import system modules.
import arcpy

try:
    # Set the workspace and input features.
    arcpy.env.workspace = 'C:\\SpatialOutlierDetection\\MyData.gdb'
    inputFeatures = "PM25_AirQualityStations"

    # Set the name of the output features
    outputFeatures = "AirQualityStations_SpatialOutliers"

    # Set the number of neighbors
    numberNeighbors = 8

    # Set the percentage of locations considered outliers
    pcntLocationsAsOutliers = 10

    # Set the output prediction raster
    outputPredictionRaster = airQualityStations_OutPredictionRaster


    # Run the Spatial Outlier Detection tool
    arcpy.stats.SpatialOutlierDetection(inputFeatures, outputFeatures, 
            numberNeighbors, pcntLocationsAsOutliers, outputPredictionRaster)

except arcpy.ExecuteError:
    # If an error occurred when running the tool, print the error message.
    print(arcpy.GetMessages())