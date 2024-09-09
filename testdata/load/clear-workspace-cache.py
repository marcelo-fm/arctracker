import arcpy
arcpy.env.workspace = "c:/connectionFiles/SQL Server.sde"
arcpy.management.ClearWorkspaceCache()