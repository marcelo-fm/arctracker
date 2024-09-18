# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy
arcpy.CheckOutExtension("ImageAnalyst")
from arcpy.ia import *

# Set local variables
in_radar=r"C:\SAR\Low Noise_manifest_CalG0_TNR.crf"
out_radar=r"C:\SAR\Low Noise_manifest_CalG0_TNR_Water.shp"
min_area="1 SquareKilometer"
in_dem_raster=r"C:\DEM\dem_COP30_ortho.tif"
geoid="GEOID"

# Execute 
arcpy.ia.ExtractWater(in_radar, out_radar, min_area, in_dem_raster, geoid)