# Name: TrainTextTransformation.py
# Description: Train a sequence-to-sequence model to translate text from English to German.  
#
# Requirements: ArcGIS Pro Advanced license

# Import system modules
import arcpy
import os

# Set local variables
in_table = "training_data.csv"
out_folder = "c\\texttransformer"

# Run Train Text Transformation Model
arcpy.geoai.TrainTextTransformationModel(in_table, out_folder, max_epochs=2,
         text_field="input", label_field="target", batch_size=16)