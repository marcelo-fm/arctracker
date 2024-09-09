# Name: ExtractDataFromGeodatabase_Example4.py
# Description: Extract data to use a new coordinate system by using the
#              Output Coordinate System environment setting. Then run the tool a second
#              time to load the data using the reuse_schema option

# Import system modules
import arcpy

# Set the Output Coordinate System environment
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("GCS_North_American_1983_HARN")
arcpy.env.geographicTransformations = "NAD_1983_HARN_To_WGS_1984_2"

# Set local variables
in_data = "C:/MyProject/MyGDB.gdb/FC1"
extract_type = "SCHEMA_ONLY"
out_type = "NEW_FILE_GEODATABASE"
out_geodatabase = ""
out_xml = ""
out_folder_path = "C:\MyProject"
out_name = "MyOutputGDB.gdb"
expand_fcs = "USE_DEFAULTS"
reuse_schema = "DO_NOT_REUSE"
get_related_data = "GET_RELATED"
extract_using_geom = ""
geom_filter = ""
all_records = "SCHEMA_ONLY_FOR_TABLES"

# Run ExtractDataFromGeodatabase with the schema only option
arcpy.management.ExtractDataFromGeodatabase(in_data,
                                            extract_type,
                                            out_type,
                                            out_geodatabase,
                                            out_xml,
                                            out_folder_path,
                                            out_name,
                                            expand_fcs,
                                            reuse_schema,
                                            get_related_data,
                                            extract_using_geom,
                                            geom_filter,
                                            all_records)

# Rest the Output Coordinate System environment
arcpy.ClearEnvironment("outputCoordinateSystem")
arcpy.ClearEnvironment("geographicTransformations")

# Set variables that we are changing to load the data into the newly created schema in 
# the different coordinate system.
extract_type = "DATA"
out_type = "GEODATABASE"
out_geodatabase = "C:\MyProject\MyOutputGDB.gdb"
out_folder_path = ""
out_name = ""
reuse_schema = "REUSE"
all_records = "ALL_RECORDS_FOR_TABLES"

# Run ExtractDataFromGeodatabase with the data and reuse schema option
arcpy.management.ExtractDataFromGeodatabase(in_data,
                                            extract_type,
                                            out_type,
                                            out_geodatabase,
                                            out_xml,
                                            out_folder_path,
                                            out_name,
                                            expand_fcs,
                                            reuse_schema,
                                            get_related_data,
                                            extract_using_geom,
                                            geom_filter,
                                            all_records)