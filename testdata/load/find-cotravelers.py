# Name: FindCotravelers.py
# Description: Identify cotravelers in a point track dataset. 

# Import system modules 
import arcpy 

arcpy.env.workspace = "C:/data/Tracks.gdb"

# Set local variables 
source_features = "Known_Tracks"
unknown_features = "Unknown_Tracks"
output_point_features = "Cotravelers"
id_field_name = "device_id"
unknown_id_field = "MMSI"
search_distance = "75 Feet"
time_difference = "5 Seconds"
summary_table = "CREATE_SUMMARY_TABLE"
summary_table_name = "Tracks_Summary_Table"
filter_duration = "MIN_COTRAVELING_DURATION"
cotraveling_duration = "30 Minutes"


# Run tool
arcpy.intelligence.FindCotravelers(source_features,
                                   output_point_features,
                                   id_field_name,
                                   search_distance,
                                   time_difference,
                                   "TWO_FEATURECLASSES",
                                   unknown_features,
                                   unknown_id_field,
                                   summary_table,
                                   summary_table_name,
                                   filter_duration,
                                   cotraveling_duration)