import arcpy
arcpy.CreateDatabaseSequence_management(r"C:/geodatabases/myfilegdb.gdb", 
                                        "my_ids", 1, 1)