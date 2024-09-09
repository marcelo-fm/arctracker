import arcpy
arcpy.env.workspace = "f:/Connections/airport.sde"
arcpy.AddFieldConflictFilter_management("Primary_UG", ["phase", "material"])