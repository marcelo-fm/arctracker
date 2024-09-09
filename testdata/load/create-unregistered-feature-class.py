import arcpy
arcpy.management.CreateUnRegisteredFeatureclass(
    r'Database Connections\Connection to Organization.sde', "New_FC", "POINT", 
    "", "DISABLED", "DISABLED")