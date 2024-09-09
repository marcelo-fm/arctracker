# Name: NetCDFTimeSeriesToFeatureClass_Ex_02.py
# Description: Creates a feature class from a netCDF DSG timeseries file from ARGO with a .ncml file. 

# Import system modules
Import arcpy  

# Set the local variables 
in_files_or_folders = r"C:\ARGO" 
target_workspace = r"C:\outputs\argo.gdb" 
out_point_name = "argo_point" 
observation_variables = "temperature;pressure" 
out_table_name = "" 
instance_variables = "" 
include_subdirectories = "DO_NOT_INCLUDE_SUBDIRECTORIES" 
in_cf_metadata = "ARGO_cf.ncml" 
analysis_extent = "" 
out_join_layer = "" 

# Execute NetCDFTimeSeriesToFeatureClass
arcpy.md.NetCDFTimeSeriesToFeatureClass(in_files_or_folders, target_workspace,
                                      out_point_name, observation_variables,
                                      out_table_name, instance_variables,
                                      include_subdirectories, in_cf_metadata,
                                      analysis_extent, out_join_layer)