#Add raster function on top of mosaic dataset

import arcpy
arcpy.env.workspace = "C:/Workspace"

mdname = "editfunction.gdb/md"
editmode = "EDIT_MOSAIC_DATASET"
editmethod = "INSERT"
funcfile = "C:/workspace/hillshade.rft.xml"
funcname = "#"

arcpy.EditRasterFunction_management(mdname, editmode, editmethod, 
                                    funcfile, funcname)