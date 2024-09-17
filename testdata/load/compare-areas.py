# Name: CompareAreas.py
# Description: Identify unique movement point track identifiers in known areas of interest. 

# Import system modules 
import arcpy 

arcpy.env.workspace = "C:/data/Tracks.gdb"

# Set local variables 
point_features = "Movement_Points"
area_features = "Areas_Of_Interest"
out_features = "Compare_Areas"
point_id_field = "Created_By"
area_id_field = "Name"
relationship = "LOCATION_TIME"
time_difference = "2 Hours"

# Run tool
arcpy.intelligence.CompareAreas(point_features,
                                area_features,
                                out_features,
                                point_id_field,
                                area_id_field,
                                relationship,
                                time_difference)