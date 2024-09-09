##==================================
##Mosaic
##Usage: Mosaic_management inputs;inputs... target {LAST | FIRST | BLEND | MEAN | MINIMUM | MAXIMUM} {FIRST | REJECT | LAST | MATCH} 
##                         {background_value} {nodata_value} {NONE | OneBitTo8Bit} {mosaicking_tolerance}  
##                         {NONE | STATISTIC_MATCHING | HISTOGRAM_MATCHING 
##                         | LINEARCORRELATION_MATCHING}

import arcpy
arcpy.env.workspace = r"\\workspace\PrjWorkspace\RasGP"

##Mosaic two TIFF images to a single TIFF image
##Background value: 0
##Nodata value: 9
arcpy.Mosaic_management("landsatb4a.tif;landsatb4b.tif","Mosaic\\landsat.tif","LAST","FIRST","0", "9", "", "", "")

##Mosaic several 3-band TIFF images to FGDB Raster Dataset with Color Correction
##Set Mosaic Tolerance to 0.3. Mismatch larget than 0.3 will be resampled
arcpy.Mosaic_management("rgb1.tif;rgb2.tif;rgb3.tif", "Mosaic.gdb\\rgb","LAST","FIRST","", "", "", "0.3", "HISTOGRAM_MATCHING")