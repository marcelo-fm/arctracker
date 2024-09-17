# Import system modules
import arcpy
from arcpy.ia import *

"""
Usage: NonMaximumSuppression(in_features,confidence_score_field, 
out_features, {class_value_field}, {max_overlap_ratio})
"""

# Set local variables
in_features = "c:/classifydata/Trees.tif"
confidence_score_field = "Confidence"
out_features = "c:/detectobjects/trees.shp"
class_value_field = "Classvalue"
max_overlap_ratio = 0.2


# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute 
NonMaximumSuppression(in_features,confidence_score_field, out_features, 
class_value_field, max_overlap_ratio)