# Name: TrainTextClassification.py
# Description: Train a text classifier model to classify text in different classes.  
#
# Requirements: ArcGIS Pro Advanced license

# Import system modules
import arcpy
import os

arcpy.env.workspace = "C:/textanalysisexamples/data"

# Set local variables
in_table = "training_data_textclassifier.csv"
out_folder = "c\\textclassifier"

# Run Train Text Classification Model
arcpy.geoai.TrainTextClassificationModel(in_table, out_folder, 
            max_epochs=2, text_field="Address", label_field="Country", batch_size=16)