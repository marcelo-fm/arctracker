# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy
arcpy.CheckOutExtension("ImageAnalyst")
from arcpy.ia import *

# Set local variables
inRaster = "c:/test/InputRaster.tif"
out_folder = "c:/test/OutputFolder"
in_training = "c:/test/TrainingData.shp"
image_chip_format = "TIFF"
tile_size_x = "256"
tile_size_y = "256"
stride_x= "128"
stride_y= "128"
output_nofeature_tiles= "ONLY_TILES_WITH_FEATURES"
metadata_format= "Labeled_Tiles"
start_index = 0
classvalue_field = "Classvalue"
buffer_radius = 0
in_mask_polygons = "MaskPolygon"
rotation_angle = 0
reference_system = "PIXEL_SPACE"
processing_mode = "PROCESS_AS_MOSAICKED_IMAGE"
blacken_around_feature = "NO_BLACKEN"
crop_mode = “FIXED_SIZE”

# Execute 
ExportTrainingDataForDeepLearning(inRaster, out_folder, in_training, 
    image_chip_format,tile_size_x, tile_size_y, stride_x, 
    stride_y,output_nofeature_tiles, metadata_format, start_index, 
    classvalue_field, buffer_radius, in_mask_polygons, rotation_angle, 
    reference_system, processing_mode, blacken_around_feature, crop_mode)