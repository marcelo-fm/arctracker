# Name: ClassifyText.py
# Description: Classify text into multiple classes
#
# Requirements: ArcGIS Pro Advanced license

# Import system modules
import arcpy

arcpy.env.workspace = "C:/textanalysisexamples/data"

# Set local variables
in_table = "TextClassifierData"
pretrained_model_path_emd = "c:\\classifydata\\TextClassifier.emd"

# Run Classify Text Using Deep Learning
arcpy.geoai.ClassifyTextUsingDeepLearning(in_table, "Address", pretrained_model_path_emd)