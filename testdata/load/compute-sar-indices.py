# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy
arcpy.CheckOutExtension("ImageAnalyst")
from arcpy.ia import *

# Set local variables
arcpy.env.workspace = r"C:\Data\SAR" 
in_radar_data = "Quad-Polarization_manifest_CalB0_TNR_RTFG0_Dspk_GTC.crf" 
out_raster = "Quad-Polarization_manifest_CalB0_TNR_RTFG0_Dspk_GTC_RVI.crf"
index = "RVI" 
polarization_bands = "HH, HV, VH, VV" 

# Execute  
out = arcpy.ia.ComputeSARIndices(
            in_radar_data, out_raster, index, polarization_bands) 
out.save(out_raster)