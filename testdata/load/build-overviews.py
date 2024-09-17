# Define Overviews for selected items only

import arcpy
arcpy.env.workspace = "C:/Workspace"

    
arcpy.BuildOverviews_management("Overviews.gdb/md", "OBJECTID<5", 
                                "DEFINE_MISSING_TILES",
                                "NO_GENERATE_OVERVIEWS", "#", "#")