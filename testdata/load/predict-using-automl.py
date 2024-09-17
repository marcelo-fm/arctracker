# Description: Predicts on feature or tabular data with the trained model 
#              obtained by the TrainUsingAutoML function.

# Import system modules
import arcpy
import os

# Set local variables
datapath  = "path_to_data_for_prediction" 
out_path = "path_to_gdb_for_predicted"

model_path = os.path.join(out_path, "model.dlpk")
in_features = os.path.join(datapath, "test_data.gdb", "test_data")
out_features = os.path.join(out_path, "predicted_feature.gdb", "predicted")

# Run Predict Using AutoML Model 
r = arcpy.geoai.PredictUsingAutoML(model_path, "PREDICT_FEATURES",
                                   in_features,
                                   None, None, out_features, None, None, None, True)