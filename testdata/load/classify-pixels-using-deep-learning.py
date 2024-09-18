# Import system modules
import arcpy
from arcpy.ia import *


# Set local variables
in_raster = "c:\\classifydata\\moncton_seg.tif"
in_model_definition = "c:\\classifydata\\moncton_sig.emd"
model_arguments = "padding 0; batch_size 16"
processing_mode = "PROCESS_AS_MOSAICKED_IMAGE"

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute 
Out_classified_raster = ClassifyPixelsUsingDeepLearning(in_raster, 
                   in_model_definition, model_arguments, processing_mode)
Out_classified_raster.save("c:\\classifydata\\classified_moncton.tif")