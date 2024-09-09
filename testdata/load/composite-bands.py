##====================================
##Composite Bands
##Usage: CompositeBands_management in_rasters;in_rasters... out_raster

import arcpy
arcpy.env.workspace = r"C:/Workspace"

##Compose multi types of single band raster datasets to a TIFF format raster dataset
arcpy.CompositeBands_management("band1.tif;comp.mdb/band2;comp.gdb/bands/Band_3","compbands.tif")