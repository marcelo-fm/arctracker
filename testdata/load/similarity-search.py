# Similarity Search of crime data in a metropolitan area

# Import system modules
import arcpy
import os

# Set property to overwrite existing output
arcpy.env.overwriteOutput = True

try:
    # Set the current workspace (to avoid having to specify the full path to
    # the feature classes each time)
    arcpy.env.workspace = r"C:\Analysis"

    # Make a layer from the crime feature class
    arcpy.management.MakeFeatureLayer("AllCrime", "Crime_selection") 

    # Select the target crime to match
    # Process: Select By Attribute
    arcpy.management.SelectLayerByAttribute("Crime_selection", "NEW_SELECTION",
                                            '"OBJECTID" = 1230043')

    # Use Similarity Search to create groups based on different 
    # variables or analysis fields
    # Process: Group Similar Features  
    arcpy.stats.SimilaritySearch("Crime_selection", "AllCrime", "CJMatches", 
                                 "NO_COLLAPSE", "MOST_SIMILAR", "ATTRIBUTE_VALUES", 4,
                                 "HEIGHT;WEIGHT;SEVERITY;DST2CHPSHP", "Name;WEAPON")
    
except:
    # If an error occurred when running the tool, print out the error message.
    print(arcpy.GetMessages())