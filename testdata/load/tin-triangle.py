'''****************************************************************************
Name: TinTriangle Example
Description: This script demonstrates how to use the 
             TinTriangle tool to extract triangles from each TIN in the 
             target workspace.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data" # the target workspace

# Create list of TINs
TINList = arcpy.ListDatasets("*", "Tin")

# Verify the presence of TINs in the list
if TINList:
    for dataset in TINList:
        # Set Local Variables
        TINList = arcpy.ListDatasets("*", "Tin")
        slopeUnits = "PERCENT"
        zfactor = 1
        hillshade = "HILLSHADE 300, 45" # defines hillshade azimuth & angle
        tagField = "Tag"
        Output = dataset + "_triangles.shp" # name of the output file
        #Execute TinTriangle
        arcpy.ddd.TinTriangle(dataset, Output, slopeUnits, zfactor,
                              hillshade, tagField)
        print("Finished.")
else:
    print("There are no TIN(s) in the " + env.workspace + " directory.")