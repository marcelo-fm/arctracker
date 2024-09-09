##====================================
##Usage: CopyRaster_management(
##			in_raster, out_rasterdataset, {config_keyword}, {background_value}, 
##			{nodata_value}, {NONE | OneBitTo8Bit}, {NONE | ColormapToRGB}, 
##			{1_BIT | 2_BIT | 4_BIT | 8_BIT_UNSIGNED | 8_BIT_SIGNED | 16_BIT_UNSIGNED | 
##			16_BIT_SIGNED | 32_BIT_UNSIGNED | 32_BIT_SIGNED | 32_BIT_FLOAT | 64_BIT}, 
##			{NONE | ScalePixelValue}, {NONE | RGBToColormap}, {TIFF | IMAGINE Image | 
##			BMP | GIF | PNG | JPEG | JPEG2000 | Esri Grid | Esri BIL | Esri BSQ | 
##			Esri BIP | ENVI | CRF | MRF}, {NONE | Transform}, {CURRENT_SLICE | ALL_SLICES}, {NO_TRANSPOSE | TRANSPOSE})

import arcpy
arcpy.env.workspace = r"C:\PrjWorkspace"

##Copy to new multidimensional dataset in cloud raster format and with transpose for faster data access
arcpy.management.CopyRaster(
	"SeaSurfaceTemp.nc", "SST_Transpose.crf","","",-3.402823e+38,"NONE","NONE","","NONE","NONE", "CRF", "NONE", "ALL_SLICES", "TRANSPOSE")