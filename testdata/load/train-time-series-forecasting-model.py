# Name: TrainTimeSeriesForecastingModel.py
# Description: Train a time series model on space-time cube data with
# different AI models.
  
# Import system modules                                                                                                                                                                                                                                                                                                                    
import arcpy
import os

# Set local variables
datapath  = "path_to_data_for_forecasting" 
out_path = "path_to_gdb_for_forecasting"

model_path = os.path.join(out_path, "model")
in_cube = os.path.join(datapath, "test_data")
out_features = os.path.join(out_path, "forecasted_feature.gdb", "forecasted")

# Run TrainTimeSeriesForecastingModel
arcpy.geoai.TrainTimeSeriesForecastingModel(
        in_cube,
        model_path,
        "CONSUMPTION",
        12,
        None,
        20,
        2,
        "InceptionTime",
        64,
        None,
        True,
        out_features
    )