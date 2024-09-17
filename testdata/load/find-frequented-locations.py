# Name FindFrequentedLocations.py
# Description: Find frequented locations in a track dataset.

import arcpy

arcpy.env.workspace = "C:/data/Tracks.gdb"

fc = "Movement_Tracks"
track_field = "user"
out_fc = "frequented_locations"
where_statement = "user = 'user_1'"
distance = "100 Meters"
loiter_time = "10 Minutes"
boundary = "1 Days"
min_dwells = 5
daily_dist = "NORMALIZED"

arcpy.intelligence.FindFrequentedLocations(fc, 
                                           track_field, 
                                           out_fc, 
                                           where, 
                                           distance, 
                                           loiter_time, 
                                           boundary, 
                                           min_dwells, 
                                           daily_dist)