#-------------------------------------------------------------------------------
# Name: Forest.py
# Description: Run Forest on sales data from 1980 and predict for sales in 1981
#
# Requirements: ArcGIS GeoAnalytics Server

# Import system modules
import arcpy
arcpy.env.workspace = "c:/data/commercial.gdb"
# Set local variables
trainingDataset = "https://analysis.org.com/server/rest/services/Hosted/sales/FeatureServer/0"
predictionDataset = "https://analysis.org.com/server/rest/services/Hosted/next_year/FeatureServer/0"
outputName = "training"
outputPredictedName = "predicted"

# Execute Forest
arcpy.geoanalytics.Forest("TRAIN_AND_PREDICT", inputDataset, outputName, "PERIMETER", None, ""STORE_CATEGORY true;AVG_INCOME false;POPULATION false", None, predictionDataset, 
"STORE_CATEGORY STORE_CATEGORY;AVG_INCOME MEAN_INCOME; POPULATION POPULATION", 100, , , 120, , 10, "SPATIOTEMPORAL_DATA_STORE")