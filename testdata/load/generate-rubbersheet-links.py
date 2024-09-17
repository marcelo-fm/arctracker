"""Name:        GenerateRubbersheetLinks_example_script2.py
Description: Generates links for rubbersheeting spatial adjustment. The links go
             from base road data to newly updated road data. The links are then
             analyzed for potential errors. They are then used to adjust the
             base roads (a copy is made) to better align with the updated roads.
"""

# Import system modules
import arcpy

# Set environment settings
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\conflationTools\ScriptExamples\data.gdb"

# Set local variables
sourceFeatures = "baseRoads"
targetFeatures = "updateRoads"
grlOutput = "grlinks_out"
grlOutputPts = "grlinks_out_pnt"

search_distance = "300 Feet"
match_fields = "FULLNAME RD_NAME"

qaLocations = "qa_locations"

# Generate rubbersheet links
arcpy.edit.GenerateRubbersheetLinks(sourceFeatures, targetFeatures, grlOutput, search_distance, match_fields)

"""
Note 1:  The result of GenerateRubbersheetLinks may contain errors; see the tool reference.
         Inspection and editing may be necessary to ensure correct links before using
         them for rubbersheeting.

         One of the common errors is intersecting or touching links. Their locations 
         can be found by the process below.
"""

# Find locations where links intersect or touch. The result contains coincident points.
arcpy.analysis.Intersect(grlOutput, qaLocations, "", "", "POINT")

# Delete coincident points
arcpy.management.DeleteIdentical(qaLocations, "Shape")

"""
Note 2:  You can manually inspect locations in qaLocations and delete or
         modify links as needed.
"""

# Make a copy of the sourceFeatures for rubbersheeting
arcpy.management.CopyFeatures(sourceFeatures, "sourceFeatures_Copy")


# Use the links for rubbersheeting
arcpy.edit.RubbersheetFeatures("sourceFeatures_Copy", grlOutput, grlOutputPts, "LINEAR")