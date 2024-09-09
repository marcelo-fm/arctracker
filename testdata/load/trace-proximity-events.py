# Name: TraceProximityEvents.py
# Description: Trace proximity events for user1 and user4 with 30 feet 
#              spatial search distance and 10 minute temporal search distance.

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = r"C:/data/TraceData.gdb"

# Use time-enabled multifile feature connection dataset
inFeatures = r"C:/data/Example.mfc/example_tracks"

entityIDField = "user_id"
outFile = "ProximityEvents" 
spatialDistance = "30 Feet"
temporalDistance = "10 Minutes"
entitiesOfInterest = [['user1', '3/30/2020 9:00:00 AM'], ['user4', '3/30/2020 9:00:00 AM']]
outTracks = "out_tracks"
max_trace_depth = 3

# Run Trace Proximity Events
arcpy.gapro.TraceProximityEvents(inFeatures, entityIDField, outFile, "PLANAR",
                                 spatialDistance, temporalDistance, 
                                 "ID_START_TIME", entitiesOfInterest, None, 
                                 outTracks, max_trace_depth)