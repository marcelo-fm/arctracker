# Import system modules 
import arcpy 
from arcpy.ia import * 

""" 
Usage: DetectObjectsUsingDeepLearning(from_raster, to_raster, out_classified_raster, 
    in_model_definition, {model_arguments}) 
"""

# Check out the ArcGIS Image Analyst extension license 
arcpy.CheckOutExtension("ImageAnalyst")

# Set local variable
from_raster = r"c:/detectchange/input_image1.tif"
to_raster = r"c:/detectchange/input_image2.tif"
out_classified_raster = r"c:/detectchange/output_difference.tif"
in_model_definition = r"c:/ detectchange/detectbuilding.emd"

# arcpy.env.processorType = "GPU"
# arcpy.env.gpuId = 0

# Execute
DetectChangeUsingDeepLearning(from_raster, to_raster, out_classified_raster, 
    in_model_definition, "padding 0;score_threshold 0.6;batch_size 4")