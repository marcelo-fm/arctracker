# Import system modules
import arcpy
from arcpy.ia import *

"""
Usage: DetectObjectsUsingDeepLearning( in_raster, out_detected_objects, 
       in_model_definition, {arguments}, {run_nms}, {confidence_score_field}, 
       {class_value_field}, {max_overlap_ratio}, {processing_mode})
"""

# Set local variables
in_raster = "c:/classifydata/moncton_seg.tif"
out_detected_objects = "c:/detectobjects/moncton.shp"
in_model_definition = "c:/detectobjects/moncton_sig.emd"
model_arguments = "padding 0; threshold 0.5; batch_size 4"
run_nms = "NO_NMS"
confidence_score_field = "Confidence"
class_value_field = "Class"
max_overlap_ratio = 0
processing_mode = "PROCESS_AS_MOSAICKED_IMAGE"
# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute 
DetectObjectsUsingDeepLearning( in_raster, out_detected_objects, 
   in_model_definition, model_arguments, run_nms, confidence_score_field, 
   class_value_field, max_overlap_ratio, processing_mode)