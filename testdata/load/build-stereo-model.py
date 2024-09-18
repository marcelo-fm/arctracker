import arcpy
arcpy.management.BuildStereoModel("c:/data/fgdb.gdb/md", 10, 70, 0.6, None, 2, None, "SAMEFLIGHT")