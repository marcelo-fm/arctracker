import arcpy
import os
arcpy.env.workspace = "c:/data"
arcpy.conversion.JSONToFeatures("myjsonfeatures.json", os.path.join("outgdb.gdb", "myfeatures"))