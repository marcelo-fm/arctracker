import arcpy
data_conn_str = arcpy.CreateDatabaseConnectionString_management("SQL_SERVER",
                                          "utah",
                                          "DATABASE_AUTH",
                                          "gdb",
                                          "gdb", 
                                          "",
                                          "gdb.roads")
arcpy.Buffer_analysis(data_conn_str, r"c:\temp\Buffers.shp", "10 Miles")