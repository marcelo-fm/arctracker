import arcpy
arcpy.management.MigrateDateFieldToHighPrecision("C:/MyProject/MyGDB.gdb/Table1", ["date_field1", "date_field2"])