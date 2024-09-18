# Description: Forecast a time series model on space-time cube data with the trained model 
#              obtained by the TrainTimeSeriesForecastingModel function.

# Import system modules
import arcpy
import os

# Set local variables
datapath  = "path_to_data_for_forecasting" 
out_path = "path_to_gdb_for_forecasting"

model_path = os.path.join(out_path, "model.dlpk")
in_cube = os.path.join(datapath, "test_data")
output_features = os.path.join(out_path, "forecasted_feature.gdb", "forecasted")

# Run Forecast Using Time Series Model 
r = arcpy.geoai.ForecastUsingTimeSeriesModel(
    in_cube,
    model_path,
    output_features,
    number_of_timesteps_to_forecast=2,
    match_explanatory_variables=None
)