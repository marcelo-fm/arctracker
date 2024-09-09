# Name: NetCDFProfilesToFeatureClass_Ex_02.py
# Description: Creates a 3D point feature class from a set of float data.

# Import system modules
Import arcpy  

# Set the local variables 
in_files_or_folders = r"C:\Argo" 
target_workspace = r"C:\outputs\argo.gdb" 
out_point_or_polyline_name = "argo_3d" 
observation_variables = "temperature;pressure" 
out_table_name = "" 
instance_variables = "" 
out_schema = "POINT_3D" 
include_subdirectories = "DO_NOT_INCLUDE_SUBDIRECTORIES" 
in_cf_metadata = "" 
analysis_extent = "" 
out_join_layer = "" 

# Execute NetCDFProfilesToFeatureClass
arcpy.md.NetCDFProfilesToFeatureClass(in_files_or_folders, target_workspace,
                                      out_point_or_polyline_name, observation_variables,
                                      out_table_name, instance_variables, out_schema,
                                      include_subdirectories, in_cf_metadata,
                                      analysis_extent, out_join_layer)