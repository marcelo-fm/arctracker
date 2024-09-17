# Name: BatchImportData_Example2.py
# Description: Imports all shapefiles with 'airport' in the file name or file
#              path within a directory to feature classes in a single geodatabase.
# Requirements: Standard or Advanced license

# Import system modules
import arcpy

# Set local variables
in_data = ["c:/data/sourcedata"]
target_gdb = r"\\data\operationaldata.sde" 
filter = "*airports*.shp" 
include_sub_folders = "NO_SUBFOLDERS" 

# Run BatchImportData
arcpy.intelligence.BatchImportData(in_data, target_gdb, filter, include_sub_folders)