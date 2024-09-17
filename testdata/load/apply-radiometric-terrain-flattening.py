# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy
arcpy.CheckOutExtension("ImageAnalyst")
from arcpy.ia import *

# Set local variables
in_radar = r"C:\Data\SAR\IW_manifest_TNR_CalB0_Dspk.crf"
out_radar = r"C:\Data\SAR\IW_manifest_TNR_CalB0_Dspk_RTFG0.crf"
in_dem_raster = r"C:\Data\DEM\dem.tif"
ApplyGeoid = "GEOID" 
polarization = "VH;VV"
calibration_type = "GAMMA_NOUGHT"

# Execute 
outRadar = arcpy.ia.ApplyRadiometricTerrainFlattening(
     in_radar, in_dem_raster, ApplyGeoid, polarization, calibration_type)
outRadar.save(out_radar)