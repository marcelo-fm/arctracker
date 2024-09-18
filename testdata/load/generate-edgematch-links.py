"""
Name:        EdgematchFeatures_example_script2.py
Description: Performs edgematching spatial adjustment using links produced by
             GenerateEdgematchLinks. The links go from input features to adjacent 
             features. The links are then checked for intersecting conditions, which
             may not be desired. They are then used to adjust input features 
             (a copy is made) to connect to the matched adjacent features.
"""

# Import system modules.
import arcpy

# Set environment settings.
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\conflationTools\ScriptExamples\data.gdb"

# Set local variables.
inFeatures = "roads1"
adjFeatures = "roads2"
gelOutput = "gelinks_out"

search_distance = "200 Feet"
match_fields = "NAME ROAD_NAME"

qaLocations = "qa_locations"

# Generate rubbersheet links.
arcpy.edit.GenerateEdgematchLinks(inFeatures, adjFeatures, gelOutput, search_distance, match_fields)

"""
Note 1:  The result of GenerateEdgematchLinks may contain errors; see the tool reference.
         Inspection and editing may be necessary to ensure correct links before using
         them for edgematching.

         One of the possible errors is intersecting or touching links.  
         Their locations can be found by the process below.
"""

# Find locations where links intersect or touch. The result contains coincident points.
arcpy.analysis.Intersect(gelOutput, qaLocations, "", "", "POINT")

# Delete coincident points.
arcpy.management.DeleteIdentical(qaLocations, "Shape")

"""
Note 2:  You can manually inspect locations in qaLocations and delete or
         modify links as needed.
"""

# Make a copy of the inFeatures for edgematching.
inFeature_Copy = inFeatures + "_Copy"
arcpy.management.CopyFeatures(inFeatures, inFeature_Copy)

# Use the links to adjust the copy of the input features.
arcpy.edit.EdgematchFeatures(inFeature_Copy, gelOutput, "MOVE_ENDPOINT")