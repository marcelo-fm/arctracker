# Resample TIFF image to a higher resolution

import arcpy
arcpy.env.workspace = r"C:/Workspace"
    
arcpy.Resample_management("image.tif", "resample.tif", "10", "CUBIC")