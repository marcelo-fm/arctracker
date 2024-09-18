# Import system modules 
import arcpy 

# Define input parameters 
in_raster = "D:\Data\SAR\S1\20181014\IW_manifest_TNR_CalB0_Dspk_RTFG0_GTC_dB.crf"
out_raster = "D:\Data\SAR\S1\20181014\IW_manifest_TNR_CalB0_Dspk_RTFG0_GTC_dB_RGB.crf"
method = "BAND_NAMES"
redExp = "VV"
greenExp = "VH"
blueExp = "VV-VH" 

arcpy.management.CreateColorComposite(in_raster, out_raster, method, 
    redExp, greenExp, blueExp)