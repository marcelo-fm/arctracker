# Import system modules 

import arcpy 
from arcpy.ia import * 

# Check out the ArcGIS Image Analyst extension license 
arcpy.CheckOutExtension("ImageAnalyst") 

# Define input parameters 
in_weather_variables = "C:/Data/ClimateVariables.crf" 
in_dem_varaible = "C:/Data/dem.tif" 
in_target = "C:/Data/pm2.5_observations.shp" 
target_value_field = "mean_pm2.5" 
Target_date_field = "date_collected" 
Raster_dimension = “StdTime” 
out_model_definition = "C:/Data/pm2.5_trained_model.ecd" 
Out_importance_table = "C:/Data/pm2.5_importance_table.csv" 
max_num_trees = 50 
max_tree_depth = 30 
max_num_samples = 10000 

# Execute - train with random tree regression model 
arcpy.ia.TrainRandomTreesRegressionModel(in_weather_variables;in_dem_varaible, in_target, out_model_definition,  target_value_field, Target_date_field, Raster_dimension, max_num_trees, max_tree_depth, max_num_samples)