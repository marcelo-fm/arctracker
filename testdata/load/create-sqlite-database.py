import arcpy

# Run CreateSQLiteDatabase
arcpy.management.CreateSQLiteDatabase('C:/data/example.sqlite', 'ST_GEOMETRY')