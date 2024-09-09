# Name: CreateFolder_Example2.py
# Description: Create a folder

# Import system modules
import arcpy

# Set local variables
out_folder_path = "C:/output" 
out_name = "folder1"

# Execute CreateFolder
arcpy.CreateFolder_management(out_folder_path, out_name)