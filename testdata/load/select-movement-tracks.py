# SelectMovementTracks.py
# Description: Select movement tracks that are identified in a known area of interest.

# Import system modules
import arcpy

arcpy.env.workspace = "C:/data/Tracks.gdb"

# Set local variables 
point_features = "Movement_Points"
area_features = "Areas_Of_Interest"

arcpy.management.MakeFeatureLayer(point_features, "lyr")
arcpy.intelligence.SelectMovementTracks("lyr", 
                                        "created_user", 
                                        area_features, 
                                        "NONE")