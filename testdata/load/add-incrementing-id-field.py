import arcpy
arcpy.management.AddIncrementingIDField("C:/Data/DatabaseConnections/mydb.sde/insp.violations", "FSID")