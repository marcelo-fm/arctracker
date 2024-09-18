import arcpy
arcpy.env.workspace = "C:/data"
arcpy.SortCodedValueDomain_management("montgomery.gdb", "material", "CODE", "ASCENDING")