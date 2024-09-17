# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set local variables 
detected_features = "C:/DeepLearning/Data.gdb/detectedFeatures" 
ground_truth_features = "C:/DeepLearning/Data.gdb/groundTruth" 
out_accuracy_table = "C:/DeepLearning/Data.gdb/accuracyTable" 
out_accuracy_report = "C:/DeepLearning/accuracyReport.pdf" 
detected_class_value_field = "Class" 
ground_truth_class_value_field = "Class" 
min_iou = 0.5 
mask_features = "C:/DeepLearning/Data.gdb/AOI" 

# Execute 
ComputeAccuracyForObjectDetection(detected_features, 
	ground_truth_features, out_accuracy_table, 
	out_accuracy_report, detected_class_value_field, 
	ground_truth_class_value_field, min_iou, mask_features)