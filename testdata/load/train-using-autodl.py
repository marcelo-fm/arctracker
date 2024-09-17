# Name: TrainUsingAutoDL.py
# Description: Train a deep learning model on imagery data with
# automatic hyperparameter selection.
  
# Import system modules
import arcpy
import os

# Set local variables

datapath = "path_to_training_data" 
out_path = "path_to_trained_model"

out_model = os.path.join(out_path, "mymodel")

# Run Train Using AutoML Model
arcpy.geoai.TrainUsingAutoDL(
    datapath, out_model, None, 2, "BASIC", 
    ["ATSS", "DCN", "FasterRCNN", "RetinaNet", "SingleShotDetector", "YOLOv3"], 
    "SAVE_BEST_MODEL")