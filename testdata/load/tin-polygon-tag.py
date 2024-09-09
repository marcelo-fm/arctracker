'''****************************************************************************
Name: TinPolygonTag Example
Description: This script demonstrates use of the 
             TinPolygonTag tool to extract tag information 
             from each TIN in the target workspace.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set Local Variables
TagField = "Code"

# Create list of TINs
TINList = arcpy.ListDatasets("*", "Tin")

# Verify the presence of TINs in the list
if TINList:
    # Iterate through the list of TINs
    for dataset in TINList:
        # Define the name of the output file
        Output = dataset + "_domain.shp"
        # Execute TinPolygonTag
        arcpy.ddd.TinPolygonTag(dataset, Output, TagFieldField)
    print("Finished.")
else:
    print("No TIN files reside in {0}".format(env.workspace))