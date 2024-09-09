import arcpy
arcpy.ddd.SetLasClassCodesUsingRaster("Jacmel.las", "reclass.tif", "COMPUTE_STATS")