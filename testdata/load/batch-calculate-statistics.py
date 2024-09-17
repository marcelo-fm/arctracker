#Calculate Statistics for multiple raster datasets with 
#multiple ignore values. 
#Skip datasets that already have the statistics.

import arcpy
arcpy.env.workspace = "C:/Workspace"

    
inras = "image1.tif;image2.img;fgdb.gdb/image3"
skipcol = "5"
skiprow = "5"
ignoreval = "0;255;21"
skipexist = "SKIP_EXISTING"

arcpy.BatchCalculateStatistics_management(
     inras, skipcol, skiprow, ignoreval,skipexist)