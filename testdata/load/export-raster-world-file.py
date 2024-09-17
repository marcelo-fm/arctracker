##====================================
##Export Raster World File
##Usage: ExportRasterWorldFile_management in_raster

import arcpy
arcpy.env.workspace = "C:/Workspace"

##Export tfw file from the intput Raster Dataset
arcpy.ExportRasterWorldFile_management("image.tif")