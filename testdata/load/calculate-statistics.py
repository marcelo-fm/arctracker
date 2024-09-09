# Calculate Statistics for single raster dataset

import arcpy
arcpy.env.workspace = "C:/Workspace"
    
arcpy.CalculateStatistics_management("image.tif", "4", "6", "0;255;21")