import arcpy
arcpy.env.workspace = "d:/Connections/airport.sde"
arcpy.RemoveFieldConflictFilter_management("Primary_UG", ["phase", "material"])