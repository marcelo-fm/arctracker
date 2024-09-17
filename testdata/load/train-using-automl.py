# Name: TrainUsingAutoML.py
# Description: Train a machine learning model on feature or tabular data with
# automatic hyperparameter selection.
  
# Import system modules
import arcpy
import os

# Set local variables

datapath  = "path_to_data" 
out_path = "path_to_trained_model"

in_feature = os.path.join(datapath, "train_data.gdb", "name_of_data")
out_model = os.path.join(out_path, "model.dlpk")

# Run Train Using AutoML Model
arcpy.geoai.TrainUsingAutoML(in_feature, out_model, "price", None, 
                             "bathrooms #;bedrooms #;square_fee #", None, None, 
                             240, "BASIC")