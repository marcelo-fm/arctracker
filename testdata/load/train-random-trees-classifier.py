# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")


# Set local variables
in_changeAnalysisRaster = "c:/test/LandsatCCDC.crf"
train_features = "c:/test/train.gdb/train_features"
out_definition = "c:/output/change_detection.ecd"
additional_raster = ''
maxNumTrees = 50
maxTreeDepth = 30
maxSampleClass = 1000
attributes = None
dimension_field = "DateTime"

# Execute
arcpy.sa.TrainRandomTreesClassifier(
	in_changeAnalysisRaster, train_features, 
	out_definition, additional_raster, maxNumTrees, 
	maxTreeDepth, maxSampleClass, attributes, dimension_field)