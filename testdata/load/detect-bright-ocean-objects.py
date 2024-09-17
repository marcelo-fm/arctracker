# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy
arcpy.CheckOutExtension("ImageAnalyst")
from arcpy.ia import *

# Set local variables
in_radar_data= r"C:\Data\SAR\IW_manifest_CalG0.crf"
out_feature_class = r"C:\Output\Ocean.gdb\DetectBrightOceanObjects"
out_type = "BOUNDS"
min_object_width = "50 Meters"
max_object_width = "500 Meters"
min_object_length = "50 Meters"
max_object_length = "500 Meters"
mask_features = "MPA Water Polygon"
feature_type = "Water"
in_dem_raster = r"C:\Data\DEM\dem_COP30_ortho.tif"
geoid = "GEOID"
mask_tolerance = "100 Meters"

# Execute 
arcpy.ia.DetectBrightOceanObjects(in_radar_data, out_feature_class, out_type, 
                    min_object_width, max_object_width, min_object_length, 
                    max_object_length, mask_features, feature_type, in_dem_raster, 
                    geoid, mask_tolerance)