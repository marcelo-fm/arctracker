#Specify multiple Nodata values for all bands in one Catalog item

import arcpy
arcpy.env.workspace = "C:/Workspace"

mdname = "Nodata.gdb/md"
noofbands = "3"
nodataval = "ALL_BANDS '0 9'"
nodatarange = "#"
query = "OBJECTID=2"
mode = "#"

arcpy.DefineMosaicDatasetNoData_management(mdname, noofbands, nodataval, 
                                           nodatarange, query, mode)