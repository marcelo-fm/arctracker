# Name: ClassifyMovementEvents.py
# Description: Identify movement events in a point track dataset. 

# Import system modules 
import arcpy 

arcpy.env.workspace = "C:/data/Tracks.gdb"

# Set local variables 
source_features = "Known_Tracks"
output_movement_events = "MovementEvents"
id_field = "device_id"
regions_of_interest = "Named_Areas_Of_Interest"
roi_name = "counties"

# Run tool
arcpy.intelligence.ClassifyMovementEvents(source_features,
                                          output_point_features,
                                          id_field,
                                          regions_of_interest,
                                          roi_name)