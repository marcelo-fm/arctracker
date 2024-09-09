import arcpy
arcpy.env.workspace = "c:/data"
arcpy.conversion.ExtractLocationsFromText("wells.txt", "water.gdb/wells")