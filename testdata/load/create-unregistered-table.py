import arcpy
arcpy.management.CreateUnRegisteredTable(
    r'Database Connections\Connection to Organization.sde', 'New_Table')