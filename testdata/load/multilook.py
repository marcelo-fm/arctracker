# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy
arcpy.CheckOutExtension("ImageAnalyst")
from arcpy.ia import *

# Set local variables
in_radar= r"C:\Data\SAR\Spotlight_CAPELLA_C02_SP_SICD_HH_20210106050239_20210106050241_CalB0.crf"
out_radar= r"C:\Data\SAR\Spotlight_CAPELLA_C02_SP_SICD_HH_20210106050239_20210106050241_CalB0_ML.crf"
polarization="HH"
range_looks=4
azimuth_looks=5

# Execute 
outRadar = arcpy.ia.Multilook(in_radar, polarization, range_looks, azimuth_looks)
outRadar.save(out_radar)