# Predict to Raster using the Predict using spatial statistics model file tool 

# Import system modules.
import arcpy
import os

# Set workspace.
arcpy.env.workspace = r"C:\Analysis"
arcpy.env.overwriteOutput = True

# Read the explanatory raster order and variable names using Describe Spatial 
# Statistics Model File tool.
in_model = "Suitability.ssm"
desc_result = arcpy.stats.DescribeSSMFile(in_model)

# Print the list of explanatory rasters.
print(desc_result[2])

# Split the explanatory raster strings into a list of variable names.
exp_ras = desc_result[2].split(";")

# Set Parameters for prediction.
prediction_type="PREDICT_RASTER"
out_raster= "suitability_predicted_raster.tif"
match_exp_ras0 = "Climate_Bio2050.tif"
match_exp_ras1 = "Climate_Temp2050.tif"
match_exp_ras2 = "Climate_Solar2050.tif"
match_rasters = [[match_exp_ras0, exp_ras[0], None], 
                 [match_exp_ras1, exp_ras[1], None], 
                 [match_exp_ras2, exp_ras[2], None]]

# Run tool.
arcpy.stats.PredictUsingSSMFile(in_model, prediction_type, "", "", out_raster, 
                "", "", match_rasters)