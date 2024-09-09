# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")


# Define input parameters
in_changeAnalysisRaster = "c:/test/LandsatCCDC.crf"
in_definition = "c:/output/change_detection.ecd"
in_additional_raster = ''

# Execute 
classifiedraster = arcpy.ia.ClassifyRaster(
	in_changeAnalysisRaster, indef_file, in_additional_raster)

#save output
classifiedraster.save("c:/test/time_series_class.crf")