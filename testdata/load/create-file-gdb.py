# Name: CreateFileGDB_Example2.py
# Description: Create a file GDB

# Import system modules
import arcpy

# Set local variables
out_folder_path = "C:/output" 
out_name = "fGDB.gdb"

# Run CreateFileGDB
arcpy.management.CreateFileGDB(out_folder_path, out_name)