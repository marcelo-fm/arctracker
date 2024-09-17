# Name: TransformText.py
# Description: Translate text from English to German
#
# Requirements: ArcGIS Pro Advanced license

# Import system modules
import arcpy
import os

arcpy.env.workspace = "C:/textanalysisexamples/data"

# Set local variables
in_table = os.path.join("translationdata")
pretrained_model_path_emd = "c:\\translatedata\\Seq2Seq.emd"

# Run Transform Text Using Deep Learning
arcpy.geoai.TransformTextUsingDeepLearning(in_table, "EnglishText", pretrained_model_path_emd)