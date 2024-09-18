# Import system modules  
import arcpy  
from arcpy.ia import *  
 
# Check out the ArcGIS Image Analyst extension license 
arcpy.CheckOutExtension("ImageAnalyst") 
 
# Define input parameters
in_raster = "C:/Classify_Objects/input_image.tif" 
out_feature_class = "C:/Classify_Objects/MyProject.gdb/classified_results" 
in_model_definition = "C:/Classify_Objects/BuildingDanmageClassifier.emd" 
in_features = "C:/Classify_Objects/building_footprints.shp" 
class_label_field = "Damaged_or_Undamaged"
model_arguments = "padding 0;batch_size 4"
process_all_raster_items = "PROCESS_AS_MOSAICKED_IMAGE"

# Execute 
ClassifyObjectsUsingDeepLearning(in_raster, out_feature_class, in_model_definition,
	in_features, class_label_field,  
	process_all_raster_items, model_arguments)