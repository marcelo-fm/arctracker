# Register raster using only control points

import arcpy
arcpy.env.workspace = "C:/Workspace"
    
rdname = "irs_ps.img"
mode = "REGISTER"
refrd = ""
linkfile = "C:/Workspace/irs_controls_13.txt"
order = "POLYORDER2"
    
arcpy.RegisterRaster_management(
     rdname, mode, refrd, linkfile, order)