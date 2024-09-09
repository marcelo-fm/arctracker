# Name: BIMFileToGeodatabase.py
# Description: Create a feature dataset

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/data/facilites"

# Create a file geodatabase for the feature dataset
arcpy.management.CreateFileGDB("C:/data/facilities", "University.gdb")

# Set local variables
out_gdb_path = "C:/data/facilites/University.gdb" 
out_dataset_name = "Building_A"
spatial_reference = "NAD_1983_StatePlane_California_VI_FIPS_0406_FEET"
identifier = "BLD_A"
include_floorplan = True

# Run BIMFileToGeodatabase 
arcpy.conversion.BIMFileToGeodatabase(["Building_A_Architectural.rvt", 
                                       "Building_A_Structural.rvt", 
                                       "Building_A_Electrical.rvt"], 
                                      out_gdb_path, out_dataset_name, 
                                      spatial_reference, identifier,include_floorplan)