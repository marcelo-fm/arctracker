# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")


# Define input parameters
in_changeAnalysisRaster = "c:/test/LandsatCCDC.crf"
train_features = "c:/test/train.gdb/train_features"
out_definition = "c:/output/change_detection.ecd"
in_additional_raster = ""
maxNumTrees = 50
maxTreeDepth = 30
maxSampleClass = 1000
attributes = None
dimension_field = "DateTime"

# Execute
arcpy.ia.TrainRandomTreesClassifier(
	in_changeAnalysisRaster, train_features, out_definition, 
	in_additional_raster, maxNumTrees, maxTreeDepth, maxSampleClass, 
	attributes, dimension_field)