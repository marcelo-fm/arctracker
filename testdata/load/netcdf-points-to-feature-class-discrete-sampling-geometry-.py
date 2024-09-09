# Name: NetCDFPointsToFeatureClass_Ex_02.py
# Description: Creates a feature class from a netCDF DSG points file from MADIS with a .ncml file. 

# Import system modules
Import arcpy  

# Set the local variables 
in_files_or_folders = r"C:\MADIS" 
target_workspace = r"C:\outputs\madis.gdb" 
out_point_name = "madis_point" 
instance_variables = "temperature;pressure"  
include_subdirectories = "DO_NOT_INCLUDE_SUBDIRECTORIES"
in_cf_metadata = r"C:\MADIS\swot_cf.ncml" 
analysis_extent = ""  

# Execute NetCDFTimeSeriesToFeatureClass
arcpy.md.NetCDFPointsToFeatureClass(in_files_or_folders, target_workspace,
                                    out_point_name, instance_variables,
                                    include_subdirectories, in_cf_metadata,
                                    analysis_extent)