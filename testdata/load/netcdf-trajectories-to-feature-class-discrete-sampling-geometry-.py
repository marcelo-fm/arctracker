# Name: NetCDFTrajectoriesToFeatureClass_Ex_02.py
# Description: Creates a polyline feature class from a netCDF DSG trajectories file of hurricane track. 

# Import system modules
Import arcpy  

# Set the local variables 
in_files_or_folders = r"C:\IBTrACS\Katrina"  
target_workspace = r"C:\outputs\hurricane.gdb" 
out_point_or_polyline_name = "Katrina_2005" 
observation_variables = "wind_speed" 
out_table_name = "" 
instance_variables = "" 
out_schema = "ROUTE_AND_EVENT" 
include_subdirectories = "DO_NOT_INCLUDE_SUBDIRECTORIES" 
in_cf_metadata = "" 
analysis_extent = "" 

# Execute NetCDFTrajectoriesToFeatureClass
arcpy.md.NetCDFTrajectoriesToFeatureClass(in_files_or_folders, target_workspace,
                                      out_point_or_polyline_name, observation_variables,
                                      out_table_name, instance_variables, out_schema,
                                      include_subdirectories, in_cf_metadata,
                                      analysis_extent)