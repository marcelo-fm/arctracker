import arcpy
arcpy.env.workspace = "C:/data/Montgomery.gdb"
arcpy.SetSubtypeField_management("water/fittings", "", "TRUE")