# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy
arcpy.CheckOutExtension("ImageAnalyst")
from arcpy.ia import *

# Set local variables
in_radar = r"C:\Data\SAR\manifest_TNR.crf"
out_radar = r"C:\Data\SAR\manifest_TNR_CalB0.crf"
polarization =  "VV;VH"
calibration = "BETA_NOUGHT"

# Execute 
outRadar = arcpy.ia.ApplyRadiometricCalibration(in_radar, polarization, calibration)
outRadar.save(out_radar)