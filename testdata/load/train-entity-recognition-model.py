# Name: TrainEntityRecognizer.py
# Description: Train an Entity Recognition model to extract useful entities like "Address", "Date" from text.  
#
# Requirements: ArcGIS Pro Advanced license

# Import system modules
import arcpy
import os

arcpy.env.workspace = "C:/textanalysisexamples/data"
dbpath = "C:/textanalysisexamples/Text_analysis_tools.gdb"

# Set local variables
in_folder = 'train_data'
out_folder = "test_bio_format"

# Run Train Entity Recognition Model
arcpy.geoai.TrainEntityRecognitionModel(in_folder, out_folder)