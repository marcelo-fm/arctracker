##Warp image with signiture file

import arcpy
arcpy.env.workspace = r"C:/Workspace"
    
    
arcpy.WarpFromFile_management("raster.img", "warp_output.tif", "gcpfile.txt", 
                      "POLYORDER2", "BILINEAR")