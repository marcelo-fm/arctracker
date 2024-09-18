#Define Overviews to the default location
#Define Overviews for all levels - ignore the primary Raster pyramid
#Define Overviews compression and resampling method

import arcpy
arcpy.env.workspace = "C:/Workspace"

    
arcpy.DefineOverviews_management("DefineOVR.gdb/md", "#", "#", "#", "#", 
                                 "#", "#", "#", "#", "FORCE_OVERVIEW_TILES",
                                     "BILINEAR", "JPEG", "50")