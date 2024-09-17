# Name: ExtractEntities.py
# Description: Extract useful entities like "Address", "Date" from text.  
#
# Requirements: ArcGIS Pro Advanced license

# Import system modules
import arcpy
import os

arcpy.env.workspace = "C:/textanalysisexamples/data"
dbpath = "C:/textanalysisexamples/Text_analysis_tools.gdb"

# Set local variables
in_folder = 'test_data'
out_table = os.path.join(dbpath, "ExtractedEntities")

pretrained_model_path_emd = "c:\\extractentities\\EntityRecognizer.emd"

# Run Extract Entities Using Deep Learning
arcpy.geoai.ExtractEntitiesUsingDeepLearning(in_folder, out_table, pretrained_model_path_emd)