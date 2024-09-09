# Name: StreamsInVegetationIntersect.py
# Purpose: Determine the vegetation type streams are traveling through.

# Import system modules
import arcpy

# Set the workspace (to avoid having to type in the full path to the data every time)
arcpy.env.workspace = "c:/data/data.gdb"    

# Process: Find all streams in each vegetation type
inFeatures = ["vegetation", "streams"]
intersectOutput = "streams_in_vegtype"

arcpy.analysis.PairwiseIntersect(inFeatures, intersectOutput)