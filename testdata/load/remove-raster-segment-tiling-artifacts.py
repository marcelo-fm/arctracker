# Import system modules
import arcpy
from arcpy.ia import *

# Set local variables
inRaster = "C:/test/segmented_raster.tif"
tile_width = "512"
tile_height = "512"

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute 
refined_seg_raster = RemoveRasterSegmentTilingArtifacts(inRaster, tile_width, tile_height)

# Save the output 
refined_seg_raster.save("C:/test/refined_segmented_raster.tif")