# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy
arcpy.CheckOutExtension("ImageAnalyst")
from arcpy.ia import *

# Set local variables
in_radar=r"C:\Data\SAR\SLC\S1A_IW_SLC__1SDV_20230708T004847_20230708T004914_049325_05EE6E_CDB3.SAFE\manifest.safe\IW3"
out_radar=r"C:\Data\SAR\SLC\IW3_manifest_Deb.crf"
polarization="VV"

# Execute 
outRadar = arcpy.ia.Deburst(in_radar, polarization)
outRadar.save(out_radar)