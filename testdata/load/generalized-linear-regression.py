# Description: Run GLR on crime data and predict if an arrest was made for a crime reporting.
#
# Requirements: ArcGIS GeoAnalytics Server

# Import system modules
import arcpy

# Set local variables
trainingDataset = "https://analysis.org.com/server/rest/services/Hosted/old_crimes/FeatureServer/0"
predictionDataset = "https://analysis.org.com/server/rest/services/Hosted/new_crimes/FeatureServer/0"
outputTrainingName = "training"

# Run GLR
arcpy.geoanalytics.GeneralizedLinearRegression(
    trainingDataset, "ArrestMade", "BINARY", ["CRIME_TYPE", "WARD", "DAY_OF_MONTH"], outputTrainingName, 
    "NO_TABLE", predictionDataset, [["CRIME_TYPE", "CRIME_TYPE"], ["WARD", "WARD"], ["DAY_OF_MONTH", "DAY_OF_MON"]], 
    [["Arrest", "NoArrest"]], "SPATIOTEMPORAL_DATA_STORE")