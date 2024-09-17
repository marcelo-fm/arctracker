#Set raster dataset type and statistics

import arcpy
arcpy.env.workspace = "C:/Workspace"
    
arcpy.SetRasterProperties_management("srtmraster.tif", "ELEVATION", 
                                         "1 50 400 5 28", "#", "#")