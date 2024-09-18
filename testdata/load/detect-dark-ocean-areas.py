# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy
arcpy.CheckOutExtension("ImageAnalyst")
from arcpy.ia import *

# Set local variables
arcpy.env.workspace = r"C:\Data\SAR"
in_radar_data="IW_manifest_CalG0"
out_raster="IW_manifest_CalG0_DDOA.crf"
min_area="20 SquareKilometers"
mask_features= "land_polygons"
feature_type="LAND"
in_dem_raster="dem_COP30_ortho.tif"
geoid="GEOID"
mask_tolerance="100 Meters"

# Execute  
out = arcpy.ia.DetectDarkOceanAreas( 
    in_radar_data, out_raster, min_area, mask_features, feature_type, 
    in_dem_raster, geoid, mask_tolerance)
out.save(out_raster)