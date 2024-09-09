#Name: VegRoadIntersect.py
# Purpose: Determine the type of vegetation within 100 meters of all stream 
#          crossings

# Import system modules
import arcpy

# Set the workspace (to avoid having to type in the full path to the data every 
# time)
arcpy.env.workspace = "c:/data/data.gdb"    
    
# Process: Find all stream crossings (points)
inFeatures = ["roads", "streams"]
intersectOutput = "stream_crossings"
arcpy.analysis.Intersect(inFeatures, intersectOutput, "", "", "point")
 
# Process: Buffer all stream crossings by 100 meters
bufferOutput = "stream_crossings_100m"
bufferDist = "100 meters"
arcpy.analysis.Buffer(intersectOutput, bufferOutput, bufferDist)

# Process: Clip the vegetation feature class to stream_crossing_100m
clipInput = "vegetation"
clipOutput = "veg_within_100m_of_crossings"
arcpy.analysis.Clip(clipInput, bufferOutput, clipOutput)

# Process: Summarize how much (area) of each type of vegetation is found
# within 100 meters of the stream crossings
statsOutput = "veg_within_100m_of_crossings_stats"
statsFields = [["shape_area", "sum"]]
caseField = "veg_type"
arcpy.analysis.Statistics(clipOutput, statsOutput, statsFields, caseField)