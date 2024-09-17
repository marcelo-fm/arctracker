# Name: FindMeetingLocations.py
# Description: Identify possible meeting locations in a movement track point dataset. 

# Import system modules 
import arcpy 

arcpy.env.workspace = "C:/data/Tracks.gdb"

# Set local variables 
movement_points = "Movement_Points"
out_area_features = "Meeting_Locations"
out_point_features = "Meeting_Details"
point_id_field = "Created_By"
search_distance = "100 Meters"
min_loiter_time = "10 Minutes"

# Run tool
arcpy.intelligence.FindMeetingLocations(movement_points,
                                        out_area_features,
                                        out_point_features,
                                        point_id_field,
                                        search_distance,
                                        min_loiter_time)