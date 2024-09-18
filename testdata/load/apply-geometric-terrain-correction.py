# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy
arcpy.CheckOutExtension("ImageAnalyst")
from arcpy.ia import *

# Set local variables
in_radar = r"C:\Data\SAR\IW_manifest_TNR_CalB0_Dspk_RTFG0.crf"
out_radar = r"C:\Data\SAR\IW_manifest_TNR_CalB0_Dspk_RTFG0_GTC.crf"
polarization = "VH"
in_dem_raster = r"C:\Data\DEM\dem10m.tif"
geoid_correction = "NONE"


# Execute 
outRadar = arcpy.ia.ApplyGeometricTerrainCorrection(in_radar, polarization, 
     in_dem_raster, geoid_correction)
outRadar.save(out_radar)