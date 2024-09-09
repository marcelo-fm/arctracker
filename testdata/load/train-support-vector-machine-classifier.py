# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")


# Define input parameters
in_changeAnalysisRaster = "c:/test/LandsatCCDC.crf"
train_features = "c:/test/train.gdb/train_features"
out_definition = "c:/output/change_detection.ecd"
additional_raster = ''
attributes = None
dimension_field = "DateTime"

# Execute
arcpy.ia.TrainSupportVectorMachineClassifier(
    in_changeAnalysisRaster, train_features, out_definition, 
	additional_raster, attributes, dimension_field)