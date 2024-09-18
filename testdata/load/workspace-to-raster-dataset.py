##==================================
##Workspace To Raster Dataset
##Usage: WorkspaceToRasterDataset_management in_workspace in_raster_dataset {NONE | INCLUDE_SUBDIRECTORIES} 
##                                           {LAST | FIRST | BLEND | MEAN | MINIMUM | MAXIMUM} {FIRST | REJECT
##                                           | LAST | MATCH} {background_value} {nodata_value} {NONE | OneBitTo8Bit} 
##                                           {mosaicking_tolerance}  {NONE | STATISTIC_MATCHING | HISTOGRAM_MATCHING
##                                           | LINEARCORRELATION_MATCHING} {NONE | ColormapToRGB}

import arcpy
arcpy.env.workspace = r"\\MyMachine\PrjWorkspace\RasGP"
##Mosaic images to File Geodatabase Raster Dataset with Background and Nodata setting and Color Correction
arcpy.WorkspaceToRasterDataset_management("WS2RD", "fgdb.gdb\\dataset", "INCLUDE_SUBDIRECTORIES", "LAST", \
                                          "FIRST", "0", "9", "", "", "HISTOGRAM_MATCHING", "")

##Mosaic Colormap image to RGB image
arcpy.WorkspaceToRasterDataset_management("WS2RD_clr","fgdb.gdb\\dataset2", "INCLUDE_SUBDIRECTORIES", "LAST",\
                                          "FIRST", "", "", "", "0.3", "", "ColormapToRGB")