# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy
arcpy.CheckOutExtension("ImageAnalyst")
from arcpy.ia import *

# Set local variables
in_radar = r"C:\Data\SAR\S1\20181014\IW_manifest_TNR_CalB0_Dspk_RTFG0_GTC.crf"
out_radar = r"C:\Data\SAR\S1\20181014\IW_manifest_TNR_CalB0_Dspk_RTFG0_GTC_dB.crf"
conversion_type = "LINEAR_TO_DB"

# Execute 
outRadar = arcpy.ia.ConvertSARUnits(in_radar, conversion_type)
outRadar.save(out_radar)