# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy
arcpy.CheckOutExtension("ImageAnalyst")
from arcpy.ia import *

# Set local variables
in_radar = r"C:\Data\SAR\manifest_TNR_CalB0.crf"
out_radar = r"C:\Data\SAR\manifest_TNR_CalB0_Dspk.crf" 
polarization = "VV;VH"
filter_type = "REFINED_LEE"

# Execute 
outRadar = arcpy.ia.Despeckle(in_radar, polarization, filter_type) 
outRadar.save(out_radar)