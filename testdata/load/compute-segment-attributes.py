# Import system modules
import arcpy
from arcpy.ia import *


"""
Usage: ComputeSegmentAttributes(in_segmented_raster, {in_additional_raster}, 
                               {used_attributes})
"""

# Set local variables
inSegRaster = "c:/test/moncton_seg.tif"
in_additional_raster = "c:/test/moncton.tif"
attributes = "COLOR;MEAN;STD;COUNT;COMPACTNESS;RECTANGULARITY"

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute 
compute_att = ComputeSegmentAttributes(inSegRaster, in_additional_raster, 
                                       attributes)
#save output 
compute_att.save("c:/test/moncton_computeseg.tif")