import arcpy
arcpy.management.BatchUpdateFields(
    "zip_codes", "MyProject.gdb\zip_codes_BatchUpdateFields",
    "DATA_TRANSFORMATION.csv", r"C:\BatchUpdate\script.py", "TARGET",
    "SOURCE", "DATATYPE", "DECIMALS", "ALIAS", "SCRIPT")