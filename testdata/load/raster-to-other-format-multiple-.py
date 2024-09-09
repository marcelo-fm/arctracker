##=========================
##Usage: RasterToGeodatabase_conversion Input_Rasters;Input_Rasters... 
##            Output_Geodatabase {Configuration_Keyword}

import arcpy
arcpy.env.workspace = "c:/data"

##Convert Multiple Raster Datasets to FGDB
arcpy.conversion.RasterToOtherFormat("test1;test2.tif;test3.img", 
                                     "OtherFormat.gdb","")