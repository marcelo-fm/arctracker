# Import system modules
import arcpy
from arcpy.ia import *

"""
Usage: SegmentMeanShift(in_raster, {spectral_detail}, {spatial_detail}, 
                    {min_segment_size}, {band_indexes})
"""

# Set local variables
inRaster = "c:/test/moncton.tif"
spectral_detail = "14.5"
spatial_detail = "10"
min_segment_size = "20"
band_indexes = "4 3 2"

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute 
seg_raster = SegmentMeanShift(inRaster, spectral_detail, spatial_detail, 
                              min_segment_size, min_segment_size)

# Save the output 
seg_raster.save("c:/output/moncton_seg.tif")