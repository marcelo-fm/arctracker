import arcpy
input_database = "c:\\temp\\ProductionGDB.sde"
log_file_type = "SESSION_LOG_FILE"
log_file_pool_size = 100

arcpy.ConfigureGeodatabaseLogFileTables_management(
    input_database, log_file_type, log_file_pool_size)