# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy
arcpy.CheckOutExtension("ImageAnalyst")
from arcpy.ia import *

# Set local variables
in_radar = r"C:\Data\SAR\S1B_IW_GRDH_1SDV_20181014T014104_20181014T014129_013142_018486_D82E.SAFE\manifest.safe\IW"
out_radar = r"C:\Data\SAR\IW_TNR.crf"
polarization = "VV;VH"

# Execute 
outRadar = arcpy.ia.RemoveThermalNoise(in_radar, polarization) 
outRadar.save(out_radar)