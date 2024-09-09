##=========================
##Raster To Geodatabase
##Usage: RasterToGeodatabase_conversion Input_Rasters;Input_Rasters... 
##       Output_Geodatabase {Configuration_Keyword}


import arcpy
arcpy.env.workspace = r"\\MyMachine\PrjWorkspace\RasGP"
    
##Convert Multiple Raster Dataset to FGDB
arcpy.conversion.RasterToGeodatabase("test.tif;test2.tif;test3.tif", 
                                 "ToGDB.gdb","MAX_FILE_SIZE_4GB")