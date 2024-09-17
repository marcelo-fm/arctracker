# Import system modules
import arcpy
from arcpy.ia import *

"""Usage: TrainIsoClusterClassifier(in_raster, max_num_classes, 
                out_classifier_definition, {in_additional_raster}, 
                {max_num_iterations}, {min_num_samples_per_cluster}, 
                {skip_factor},{used_attributes})

"""

# Set local variables
inSegRaster = "c:/test/moncton_seg.tif"
maxNumClasses = "10"
out_definition = "c:/output/moncton_sig_iso.ecd"
in_additional_raster = "moncton.tif"
maxIteration = "20"
minNumSamples = "10"
skipFactor = "5"
attributes = "COLOR;MEAN;STD;COUNT;COMPACTNESS;RECTANGULARITY"

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute 
TrainIsoClusterClassifier(inSegRaster, maxNumClasses, 
                out_definition,in_additional_raster, 
                maxIteration, minNumSamples, skipFactor, attributes)