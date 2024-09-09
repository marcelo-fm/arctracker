import arcpy
arcpy.env.workspace = "c:/data"
arcpy.conversion.ExtractLocationsFromDocument("wells.docx", "water.gdb/wells")